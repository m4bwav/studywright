#!/usr/bin/env python3
"""studywright CLI (standard library only).

  sw.py check DECK.json            validate a deck
  sw.py build DECK.json OUT.html   validate, then write a standalone game page
  sw.py names [FILE ...]           lint feat, badge and title names in engine files
                                   (default: templates/*.html and kit.js)
  sw.py records [--from DIR] [--to DIR]
        file the studywright-*.json records the games save (default from
        ~/Downloads) into DIR/<deck>/ as JSON + Markdown and rebuild DIR/INDEX.md,
        the paper trail agents read before writing the next test (default ./records)
"""
import json, re, sys, html
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "templates" / "game.html"
LESSON = HERE.parent / "templates" / "lesson.html"
LESSON_KINDS = {"mean", "spread", "madTeach", "mad", "read", "both"}  # encounter kinds lesson.html knows


WARNS = []  # item-writing hints: printed, never fail a build


def lint_mc(q, tag):
    ch = [str(c) for c in q.get("choices", [])]
    if len(ch) < 3:
        return
    lens = sorted(len(c) for c in ch)
    if lens[-1] > 2 * max(lens[-2], 8):
        WARNS.append(f"{tag}: one choice is much longer than the rest (a length clue); even them out")
    low = [c.lower() for c in ch]
    if any(x in ("all of the above", "none of the above") for x in low):
        WARNS.append(f"{tag}: avoid 'all/none of the above'; write one clearly best answer")


def check_item(q, tag):
    errs = []
    t = q.get("type", "mc")
    if t == "mc":
        ch = q.get("choices", [])
        if len(ch) < 2:
            errs.append(f"{tag}: mc needs 2+ choices")
        if not isinstance(q.get("answer"), int) or not 0 <= q["answer"] < len(ch):
            errs.append(f"{tag}: answer must index into choices")
        if len(set(ch)) != len(ch):
            errs.append(f"{tag}: duplicate choices")
        lint_mc(q, tag)
    elif t == "type":
        if not q.get("accept"):
            errs.append(f"{tag}: type needs 'accept' list")
    else:
        errs.append(f"{tag}: unknown type {t}")
    return errs


def check_lesson(deck):
    errs = []
    for k in ("id", "title", "subject", "intro", "skills", "map", "contexts", "gold"):
        if k not in deck:
            errs.append(f"lesson deck missing '{k}'")
    sk = deck.get("skills", {})
    for i, ly in enumerate(deck.get("map", []), 1):
        if ly.get("skill") not in sk:
            errs.append(f"map stage {i}: skill '{ly.get('skill')}' not in skills")
        if ly.get("kind") not in LESSON_KINDS:
            errs.append(f"map stage {i}: unknown kind '{ly.get('kind')}' (known: {', '.join(sorted(LESSON_KINDS))})")
    missing = set(sk) - {ly.get("skill") for ly in deck.get("map", [])}
    if missing:
        errs.append(f"skills never taught on the map: {', '.join(sorted(missing))}")
    for k in ("guided", "solo"):
        if not isinstance(deck.get("gold", {}).get(k), int):
            errs.append(f"gold.{k} must be a whole number")
    for i, c in enumerate(deck.get("contexts", []), 1):
        for k in ("intro", "what", "unit", "names", "lo", "hi", "boost", "group", "pickIntro"):
            if k not in c:
                errs.append(f"context {i}: missing '{k}'")
        if c.get("hi", 0) - c.get("lo", 0) < 20:
            errs.append(f"context {i}: hi - lo must be 20+ so spread pairs fit")
        if len(c.get("names", [])) < 2 or len(c.get("group", [])) < 4:
            errs.append(f"context {i}: needs 2 names and 4 group names")
    if "banned" in deck:
        errs.append("use banned_hashes, never raw worksheet data sets, in a committed deck")
    return errs


def check(deck):
    if deck.get("mode") == "lesson":
        return check_lesson(deck) + check_glossary(deck)
    errs = []
    if deck.get("mode") == "world":
        errs.append("world decks moved to the studyquest game on 2026-11-12; this plugin builds quest and lesson decks")
    for k in ("id", "title", "subject", "intro", "questions"):
        if k not in deck:
            errs.append(f"deck missing '{k}'")
    qs = deck.get("questions", [])
    if len(qs) < 8:
        errs.append(f"only {len(qs)} questions; aim for 15+ so every sheet item is covered twice")
    seen = set()
    for i, q in enumerate(qs, 1):
        tag = f"q{i}"
        if q.get("q") in seen:
            errs.append(f"{tag}: duplicate prompt")
        seen.add(q.get("q"))
        if not q.get("explain"):
            errs.append(f"{tag}: needs 'explain' (the why, shown after every answer)")
        errs += check_item(q, tag)
        for k in ("variants", "steps"):
            v = q.get(k, [])
            if not isinstance(v, list):
                errs.append(f"{tag}: '{k}' must be a list of questions")
                continue
            for j, sub in enumerate(v, 1):
                if not sub.get("q"):
                    errs.append(f"{tag}.{k}{j}: needs 'q'")
                errs += check_item(sub, f"{tag}.{k}{j}")
    errs += check_objectives(deck)
    errs += check_hooks(deck)
    errs += check_reuse(deck)
    errs += check_glossary(deck)
    check_praise(deck)
    return errs


def gloss_key(s):
    return " ".join(str(s).lower().split())


def gloss_index(glossary):
    """term and aliases -> entry; the first entry wins (same rule as templates/glossary.js)."""
    idx = {}
    for e in glossary or []:
        for t in [e.get("term")] + list(e.get("aliases") or []):
            if t and gloss_key(t) not in idx:
                idx[gloss_key(t)] = e
    return idx


def gloss_find(text, idx):
    """Python twin of GL.find in glossary.js: longest phrase up to 4 words; a final word ending
    in s falls back to the singular. Returns (start, end, term) tuples."""
    ws = list(re.finditer(r"[A-Za-z][A-Za-z'-]*", text))
    out, i = [], 0
    while i < len(ws):
        hit = None
        for n in range(min(4, len(ws) - i), 0, -1):
            a, b = ws[i], ws[i + n - 1]
            seg = text[a.start():b.end()]
            if n > 1 and not re.fullmatch(r"[A-Za-z'-]+(\s+[A-Za-z'-]+)*", seg):
                continue
            k = gloss_key(seg)
            e = idx.get(k)
            if e is None and re.search(r"[^s]s$", k):
                e = idx.get(k[:-1])
            if e is not None:
                hit = (a.start(), b.end(), e["term"], n)
                break
        if hit:
            out.append(hit[:3])
            i += hit[3]
        else:
            i += 1
    return out


def check_glossary(deck):
    """Optional `glossary`: [{term, def, plain, aliases?}]. Missing text fails; long plain text and duplicates warn."""
    g = deck.get("glossary")
    if g is None:
        return []
    if not isinstance(g, list):
        return ["'glossary' must be a list of {term, def, plain}"]
    errs, seen = [], set()
    for i, e in enumerate(g, 1):
        tag = f"glossary{i}"
        if not isinstance(e, dict) or not str(e.get("term", "")).strip():
            errs.append(f"{tag}: needs 'term'")
            continue
        tag += f" ({e['term']})"
        for k, why in (("def", "the original wording"), ("plain", "simpler words a child can read")):
            if not str(e.get(k, "")).strip():
                errs.append(f"{tag}: needs '{k}' ({why})")
        al = e.get("aliases")
        if al is not None and not isinstance(al, list):
            errs.append(f"{tag}: 'aliases' must be a list")
            al = None
        if str(e.get("def", "")).strip() and len(str(e.get("plain", ""))) > len(str(e["def"])):
            WARNS.append(f"{tag}: plain text is longer than def; plain should be the easier read")
        for t in [e["term"]] + (al or []):
            k = gloss_key(t)
            if k in seen:
                WARNS.append(f"{tag}: duplicate term '{t}'; the first entry wins")
            seen.add(k)
    return errs


XDECK_SKIP = {"glossary", "id", "accept", "banned_hashes", "answer"}


def deck_text(v, key=None):
    """All lesson and quiz strings in a deck, minus the glossary, ids and answers."""
    if key in XDECK_SKIP:
        return
    if isinstance(v, str):
        yield v
    elif isinstance(v, list):
        for x in v:
            yield from deck_text(x)
    elif isinstance(v, dict):
        for k, x in v.items():
            yield from deck_text(x, k)


def check_xdeck(deck, path):
    """WARN once per term that a sibling deck (same folder) glosses, this deck's text uses,
    and this deck's glossary lacks. Same matcher as the word cards."""
    path = Path(path)
    other = {}
    for f in sorted(path.parent.glob("*.json")):
        if f.resolve() == path.resolve():
            continue
        try:
            g = json.loads(f.read_text(encoding="utf-8")).get("glossary")
        except (ValueError, OSError, AttributeError):
            continue
        for e in g if isinstance(g, list) else []:
            if isinstance(e, dict) and e.get("term"):
                for t in [e["term"]] + list(e.get("aliases") or []):
                    other.setdefault(gloss_key(t), (e, f.name))
    if not other:
        return
    own = gloss_index(deck.get("glossary") if isinstance(deck.get("glossary"), list) else [])
    idx = {k: e for k, (e, _) in other.items()}
    where = {id(e): n for e, n in other.values()}
    done = set()
    for text in deck_text(deck):
        for _, _, term in gloss_find(text, idx):
            k = gloss_key(term)
            if k in done:
                continue
            done.add(k)
            e = other[k][0]
            if any(gloss_key(t) in own for t in [e["term"]] + list(e.get("aliases") or [])):
                continue
            WARNS.append(f"glossary: '{term}' is used here and defined in {where[id(e)]}, but missing from this deck's glossary")


def check_hooks(deck):
    """Optional per-question 'hook': a mnemonic (a vivid image or a link to something known)
    shown after a first miss, never before the first try. Fails on a non-string hook;
    warns when a deck has 5+ typed-recall items and none has a hook (bare-fact deck)."""
    errs, typed, hooked = [], 0, 0
    for i, q in enumerate(deck.get("questions", []), 1):
        h = q.get("hook")
        if h is not None:
            if not isinstance(h, str) or not h.strip():
                errs.append(f"q{i}: 'hook' must be a non-empty string")
            else:
                hooked += 1
        typed += q.get("type") == "type"
    if typed >= 5 and hooked == 0:
        WARNS.append(f"{typed} typed-recall items and no 'hook': give the hardest bare facts a mnemonic hint")
    return errs


def check_reuse(deck):
    """Misconception reuse, paired items, the why follow-up and predict items (Ambrose et al.,
    How Learning Works ch. 1 and 4; Zinsser, Writing to Learn ch. 11).
    - 'mis': tag(s) of the misconception an item's lures catch. One explanation rarely shifts it,
      so WARN when a tag sits on fewer than 3 items (variants count).
    - 'pair': id shared by two items that look alike but need different rules, or look different
      but share one. ERROR when a pair id is on one item; WARN when a math/science deck of 20+
      items has none.
    - 'why': follow-up mc {q?, choices, answer, explain?} asked after a right pick; the item is
      mastered only when the reason is right too. WARN (KEY-NO-WHY) when a topic of 5+ items has none.
    - WARN when a science deck of 15+ items has no predict item ('predict', 'what will happen')."""
    errs, mis, pairs, topics = [], {}, {}, {}
    qs = deck.get("questions", [])
    for i, q in enumerate(qs, 1):
        tags = q.get("mis", [])
        tags = [tags] if isinstance(tags, str) else tags
        for v in q.get("variants") or []:
            vt = v.get("mis", [])
            tags = tags + ([vt] if isinstance(vt, str) else vt)
        for t in tags:
            mis[t] = mis.get(t, 0) + 1
        if q.get("pair") is not None:
            pairs.setdefault(q["pair"], []).append(i)
        w = q.get("why")
        tp = topics.setdefault(q.get("topic", ""), [0, 0])
        tp[0] += 1
        if w is not None:
            if not isinstance(w, dict):
                errs.append(f"q{i}: 'why' must be an mc object with choices and answer")
            else:
                errs += check_item({**w, "type": "mc"}, f"q{i}.why")
                tp[1] += 1
    for t, n in mis.items():
        if n < 3:
            WARNS.append(f"MISCONCEPTION-ONCE: '{t}' is caught by {n} item(s); re-use it in 3+ items in new settings")
    for pid, items in pairs.items():
        if len(items) < 2:
            errs.append(f"pair '{pid}' is on one item (q{items[0]}); a pair needs two items")
    subj = (deck.get("realm") or deck.get("subject") or "").lower()
    if len(qs) >= 20 and not pairs and re.search(r"math|science|biology|chem|physic", subj):
        WARNS.append(f"{len(qs)} items and no 'pair': add two that look alike but need different rules")
    for t, (n, w) in topics.items():
        if n >= 5 and w == 0:
            WARNS.append(f"KEY-NO-WHY: topic '{t}' has {n} items and no 'why' follow-up; a lucky guess counts as mastered")
    if len(qs) >= 15 and re.search(r"science|biology|chem|physic", subj) and not any(
            re.search(r"\bpredict|what will happen|what happens (next|if)", q.get("q", ""), re.I) for q in qs):
        WARNS.append("science deck with no predict item: ask 'what will happen if...?' before the reason shows")
    return errs


TRAIT = re.compile(r"\b(smart|genius|gifted|clever|brilliant|a natural)\b", re.I)


def check_praise(deck):
    """Warn on praise for traits ('you're so smart') in text the child reads; praise effort,
    strategy and fixing a miss instead (Make It Stick ch. 7)."""
    for i, q in enumerate(deck.get("questions", []), 1):
        for k in ("win", "explain", "scene"):
            m = TRAIT.search(q[k]) if isinstance(q.get(k), str) else None
            if m:
                WARNS.append(f"q{i}.{k}: praises a trait ('{m.group(0)}'); praise effort or the fix instead")
    for k in ("intro", "practice"):
        if isinstance(deck.get(k), str) and TRAIT.search(deck[k]):
            WARNS.append(f"{k}: praises a trait; praise effort or the fix instead")
    for k in ("feats", "badges", "titles"):
        v = deck.get(k)
        items = v.items() if isinstance(v, dict) else enumerate(v) if isinstance(v, list) else []
        for key, it in items:
            nm = it.get("name") if isinstance(it, dict) else it
            if isinstance(nm, str):
                why = name_problem(nm)
                if why:
                    WARNS.append(f"{k}.{key}: name '{nm}' {why}")


# Reward names are read like praise (Kapp, The Gamification of Learning and Instruction, ch. 10):
# no trait words, no mocking a miss; a near-miss award says "almost" kindly.
MOCK = re.compile(r"\b(fail(s|ed|ure)?|loser|blew( it)?|noob|n00b|dumb|stupid|clumsy|butterfingers|scrub|"
                  r"worst|pathetic|useless|slowpoke|try ?hard)\b", re.I)


def name_problem(name):
    m = TRAIT.search(name)
    if m:
        return f"praises a trait ('{m.group(0)}'); name the effort or strategy instead"
    m = MOCK.search(name)
    if m:
        return f"mocks the player ('{m.group(0)}'); word a near miss as encouragement"
    return None


NAME_LIT = re.compile(r"""\b(name|title|badge|feat|label)\s*:\s*(['"`])((?:(?!\2).){1,60})\2""")


def lint_names(text):
    """Feat, badge and title names in an engine file: string literals after name:, title:,
    badge:, feat: or label: keys. Returns (line, name, problem) for each bad one."""
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        for m in NAME_LIT.finditer(line):
            why = name_problem(m.group(3))
            if why:
                hits.append((n, m.group(3), why))
    return hits


def names(argv):
    root = HERE.parent / "templates"
    files = [Path(a) for a in argv] or sorted(root.glob("*.html")) + [root / "kit.js"]
    total = found = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        found += sum(1 for _ in NAME_LIT.finditer(text))
        for n, nm, why in lint_names(text):
            total += 1
            print(f"WARN {f.name}:{n}: '{nm}' {why}")
    print(f"{len(files)} files, {found} names read, {total} reward-name warnings")
    return 0


def check_objectives(deck):
    """Optional deck key 'objectives' (list of short strings) and per-question 'objective'.
    Fails when an objective has no question or a question names an unknown objective."""
    objs = deck.get("objectives")
    if objs is None:
        return []
    if not isinstance(objs, list) or not all(isinstance(o, str) and o for o in objs):
        return ["'objectives' must be a list of non-empty strings"]
    errs, hit = [], {o: 0 for o in objs}
    for i, q in enumerate(deck.get("questions", []), 1):
        o = q.get("objective")
        if o is None:
            continue
        if o not in hit:
            errs.append(f"q{i}: objective '{o}' is not in the deck's 'objectives' list")
        else:
            hit[o] += 1
    errs += [f"objective '{o}' has no question that tests it" for o, n in hit.items() if n == 0]
    return errs


def record_md(r):
    h = r.get("hero") or {}
    total = r["questions_total"]
    L = [f"# {r['title']} - {r['finished'][:16].replace('T', ' ')}", "",
         f"- Deck: `{r['deck']}`" + (f" (follow-up to `{r['follows']}`)" if r.get("follows") else ""),
         f"- Area: {r.get('area')}; hero: {h.get('name')} the {h.get('cls')} ({h.get('xp')} XP total)",
         f"- First-try score: **{r['score_first_try']}%** ({total - len(r['first_try_misses'])}/{total}); "
         f"best streak {r['best_streak']}; {r['answers']} answers to master all", ""]
    if r["first_try_misses"]:
        L += ["## Missed on first try", ""]
        for m in r["first_try_misses"]:
            tries = "; ".join(f"'{t['given']}' {'ok' if t['ok'] else 'wrong'}" for t in m.get("tries") or [])
            L.append(f"- [{m.get('topic', '')}] {m.get('q', '')} -> **{m.get('answer', '')}**" + (f" (tries: {tries})" if tries else ""))
    else:
        L.append("Perfect first-try run.")
    if r.get("lucky_guesses"):
        L += ["", "Right pick, wrong reason: " + "; ".join(r["lucky_guesses"])]
    if r.get("wrapper"):
        L += ["", "Think-back: " + "; ".join(f"{k}: {v}" for k, v in r["wrapper"].items())]
    if r.get("unseen"):
        L += ["", f"Not reached ({len(r['unseen'])} of {r.get('deck_total')}): " + "; ".join(sorted({u.get('topic', '') for u in r["unseen"]}))]
    if r.get("mode") == "world":
        L += ["", f"Open world: {r.get('elapsed_sec', 0) // 60} min, {r.get('steps_walked')} steps, {r.get('tiles_mapped')} new tiles mapped; "
              f"regions in order: {', '.join(r.get('regions_visited') or [])}; signposts read: {', '.join(r.get('notes_read') or []) or 'none'}"]
        if r.get("bought"):
            L += ["", "Bought from merchants: " + ", ".join(f"{b.get('item')} ({b.get('price')} gold)" for b in r["bought"])]
    return "\n".join(L) + "\n"


def records(argv):
    src = Path(argv[argv.index("--from") + 1]) if "--from" in argv else Path.home() / "Downloads"
    dst = Path(argv[argv.index("--to") + 1]) if "--to" in argv else Path("records")
    new = 0
    for f in sorted(src.glob("studywright-*.json")):
        try:
            r = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        rs = r.get("records", []) if r.get("studywright_records") else [r] if r.get("studywright_record") else []
        for r in rs:
            d = dst / r["deck"]
            base = r["finished"][:16].replace(":", "-").replace("T", "-")
            if (d / f"{base}.json").exists():
                continue
            d.mkdir(parents=True, exist_ok=True)
            (d / f"{base}.json").write_text(json.dumps(r, indent=1, ensure_ascii=False), encoding="utf-8", newline="\n")
            (d / f"{base}.md").write_text(record_md(r), encoding="utf-8", newline="\n")
            new += 1
    rows = []
    for j in sorted(dst.glob("*/*.json")):
        try:
            r = json.loads(j.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if not (isinstance(r, dict) and r.get("studywright_record")):
            continue  # other JSON kept beside the records (e.g. banned-sets.json)
        miss =", ".join(sorted({m["topic"] for m in r["first_try_misses"]})) or "-"
        hero = (r.get("hero") or {}).get("name", "")
        rows.append(f"| {r['finished'][:10]} | [{r['title']}]({j.parent.name}/{j.stem}.md) | {hero} | {r['score_first_try']}% | {miss} |")
    if rows:
        (dst / "INDEX.md").write_text(
            "# Study records\n\nOne row per finished game. Each linked file lists the questions missed on the first try "
            "and what was typed. Write the next follow-up deck from the missed topics.\n\n"
            "| Date | Game | Hero | First try | Missed topics |\n|---|---|---|---|---|\n" + "\n".join(rows) + "\n",
            encoding="utf-8", newline="\n")
    print(f"filed {new} new record(s); {len(rows)} listed in {dst / 'INDEX.md'}")
    return 0


def main(argv):
    if argv and argv[0] == "records":
        return records(argv[1:])
    if argv and argv[0] == "names":
        return names(argv[1:])
    if len(argv) < 2 or argv[0] not in ("check", "build"):
        print(__doc__)
        return 2
    deck = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    errs = check(deck)
    check_xdeck(deck, argv[1])
    for e in errs:
        print("ERROR", e)
    for w in WARNS:
        print("WARN", w)
    if errs:
        return 1
    lesson = deck.get("mode") == "lesson"
    if lesson:
        print(f"ok: lesson, {len(deck['map'])} stages, skills: {', '.join(deck['skills'])}")
    else:
        n = len(deck["questions"])
        topics = sorted({q.get("topic", "") for q in deck["questions"]})
        print(f"ok: {n} questions, topics: {', '.join(topics)}")
    if argv[0] == "build":
        page = (LESSON if lesson else TEMPLATE).read_text(encoding="utf-8")
        data = json.dumps(deck, ensure_ascii=False).replace("</", "<\\/")
        kit = (HERE.parent / "templates" / "kit.js").read_text(encoding="utf-8")
        if deck.get("glossary"):
            kit += "\n" + (HERE.parent / "templates" / "glossary.js").read_text(encoding="utf-8")
        page = page.replace("/*__KIT__*/", kit)
        page = (page.replace("__TITLE__", html.escape(deck["title"]))
                    .replace("__ACCENT__", deck.get("accent", "#7aa2ff"))
                    .replace("__DECK__", data))
        Path(argv[2]).write_text(page, encoding="utf-8", newline="\n")
        print("wrote", argv[2])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
