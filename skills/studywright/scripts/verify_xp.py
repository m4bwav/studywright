"""XP rules for the templates: XP only goes up, is never spent, and never turns into gold or back.
Usage: python scripts/verify_xp.py [FILE ...]   (default: every templates/*.html and kit.js)"""
import re, sys
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


def main(argv):
    root = Path(__file__).resolve().parent.parent / "templates"
    files = [Path(a) for a in argv] or sorted(root.glob("*.html")) + [root / "kit.js"]
    bad = 0
    for f in files:
        for n, why, ctx in scan(f.read_text(encoding="utf-8")):
            bad += 1
            print(f"{f.name}:{n}: {why}: {ctx}")
    print(f"{len(files)} files, {bad} XP rule breaks")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
