"""XP rules for the templates: XP only goes up, is never spent, and never turns into gold or back.
Also warns when an easier choice the child can make pays more XP per minute than a harder one.

Usage: python scripts/verify_xp.py [FILE ...]   (default: every templates/*.html and kit.js,
                                                 plus the XP-per-minute table for game.html)
       python scripts/verify_xp.py --rates TABLE.json   (XP-per-minute check on your own table)

TABLE.json: {"choices": [{"group": "which deck", "name": "replay a mastered deck", "level": 1,
             "xp": 21, "secs": 8, "acc": 0.95}, ...]}
  group  choices the child picks between (only compared inside a group)
  level  difficulty, higher = harder
  xp     XP paid for one right answer;  secs  seconds per item, reading the reason included
  acc    share of items answered right at a typical first try
Rate warnings never fail the run; XP rule breaks do."""
import json, re, sys
from pathlib import Path

RULES = [
    (re.compile(r"\bxp\s*(-=|\*=|/=|--)|--\s*[\w.]*\bxp\b"), "XP goes down"),
    (re.compile(r"\bxp\s*=(?!=)\s*(?!0\b)[^;,}]*"), "XP overwritten (only xp=0 at creation, or +=)"),
    (re.compile(r"\bxp\s*:\s*-"), "XP starts negative"),
    (re.compile(r"\bgold\s*(\+|-)?=[^;]*\bxp\b"), "gold paid from XP"),
    (re.compile(r"\bxp\s*\+=[^;]*\bgold\b(?!\s*\?)"), "XP bought with gold"),
]


def scan(text):
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        for rx, why in RULES:
            for m in rx.finditer(line):
                # local "const xp=..." in a finish screen is a sum of gains, not a write to the hero
                if why.startswith("XP overwritten") and re.search(r"(const|let|var)\s+$", line[:m.start()]):
                    continue
                hits.append((n, why, line[max(0, m.start() - 20):m.end() + 20].strip()))
    return hits


# ---------- easy choices must not pay more XP per minute (Kapp, ch. 4: learners rewarded for
# right answers kept picking easier problems once the rewards stopped) ----------

def xp_per_min(c):
    return c["xp"] * c.get("acc", 1.0) * 60.0 / c["secs"]


def easy_pays_more(choices, tol=0.10):
    """Warnings for each pair in a group where the easier choice (lower level) earns more than
    (1 + tol) times the XP per minute of a harder one."""
    out, groups = [], {}
    for c in choices:
        groups.setdefault(c.get("group", ""), []).append(c)
    for g, cs in groups.items():
        for a in cs:
            for b in cs:
                if a["level"] < b["level"] and xp_per_min(a) > xp_per_min(b) * (1 + tol):
                    out.append(f"{g}: easier '{a['name']}' pays {xp_per_min(a):.0f} XP/min, "
                               f"harder '{b['name']}' {xp_per_min(b):.0f} XP/min")
    return out


def game_choices(text):
    """The choices game.html leaves to the child, with XP read from its award line and time and
    accuracy as stated guesses. Expected XP per right answer counts the gold streak: a right
    answer is gold when the two before it were right too (about acc squared)."""
    m = re.search(r"gain=\(gold\?(\d+):(\d+)\)", text)
    if not m:
        return []
    gold, base = int(m.group(1)), int(m.group(2))
    area = 2  # a typical study-area level, added to every right answer

    def row(name, level, acc, secs):
        return {"group": "which deck to play", "name": name, "level": level, "acc": acc, "secs": secs,
                "xp": base + (gold - base) * acc * acc + area}
    return [row("replay a deck already mastered", 1, 0.95, 8),
            row("a new deck", 2, 0.70, 15)]


def main(argv):
    if argv[:1] == ["--rates"]:
        table = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
        warns = easy_pays_more(table["choices"])
        for c in table["choices"]:
            print(f"  {c.get('group', '')} / {c['name']}: {xp_per_min(c):.0f} XP/min")
        for w in warns:
            print("WARN", w)
        print(f"{len(table['choices'])} choices, {len(warns)} easy-pays-more warnings")
        return 0
    root = Path(__file__).resolve().parent.parent / "templates"
    files = [Path(a) for a in argv] or sorted(root.glob("*.html")) + [root / "kit.js"]
    bad = 0
    for f in files:
        for n, why, ctx in scan(f.read_text(encoding="utf-8")):
            bad += 1
            print(f"{f.name}:{n}: {why}: {ctx}")
    print(f"{len(files)} files, {bad} XP rule breaks")
    if not argv:
        for w in easy_pays_more(game_choices((root / "game.html").read_text(encoding="utf-8"))):
            print("WARN game.html", w)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
