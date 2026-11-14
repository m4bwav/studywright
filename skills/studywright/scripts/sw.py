#!/usr/bin/env python3
"""studywright CLI (standard library only).

  sw.py check DECK.json            validate a deck
  sw.py build DECK.json OUT.html   validate, then write a standalone game page
  sw.py records [--from DIR] [--to DIR]
        file the studywright-*.json records the games save (default from
        ~/Downloads) into DIR/<deck>/ as JSON + Markdown and rebuild DIR/INDEX.md,
        the paper trail agents read before writing the next test (default ./records)
"""
import json, sys, html
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
        return check_lesson(deck)
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
    return errs


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
    if len(argv) < 2 or argv[0] not in ("check", "build"):
        print(__doc__)
        return 2
    deck = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    errs = check(deck)
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
        page = page.replace("/*__KIT__*/", (HERE.parent / "templates" / "kit.js").read_text(encoding="utf-8"))
        page = (page.replace("__TITLE__", html.escape(deck["title"]))
                    .replace("__ACCENT__", deck.get("accent", "#7aa2ff"))
                    .replace("__DECK__", data))
        Path(argv[2]).write_text(page, encoding="utf-8", newline="\n")
        print("wrote", argv[2])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
