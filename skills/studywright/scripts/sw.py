#!/usr/bin/env python3
"""studywright CLI (standard library only).

  sw.py check DECK.json            validate a deck
  sw.py build DECK.json OUT.html   validate, then write a standalone game page
"""
import json, sys, html
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "templates" / "game.html"


def check(deck):
    errs = []
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
        t = q.get("type", "mc")
        if t == "mc":
            ch = q.get("choices", [])
            if len(ch) < 2:
                errs.append(f"{tag}: mc needs 2+ choices")
            if not isinstance(q.get("answer"), int) or not 0 <= q["answer"] < len(ch):
                errs.append(f"{tag}: answer must index into choices")
            if len(set(ch)) != len(ch):
                errs.append(f"{tag}: duplicate choices")
        elif t == "type":
            if not q.get("accept"):
                errs.append(f"{tag}: type needs 'accept' list")
        else:
            errs.append(f"{tag}: unknown type {t}")
    return errs


def main(argv):
    if len(argv) < 2 or argv[0] not in ("check", "build"):
        print(__doc__)
        return 2
    deck = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    errs = check(deck)
    for e in errs:
        print("ERROR", e)
    if errs:
        return 1
    n = len(deck["questions"])
    topics = sorted({q.get("topic", "") for q in deck["questions"]})
    print(f"ok: {n} questions, topics: {', '.join(topics)}")
    if argv[0] == "build":
        page = TEMPLATE.read_text(encoding="utf-8")
        data = json.dumps(deck, ensure_ascii=False).replace("</", "<\\/")
        page = (page.replace("__TITLE__", html.escape(deck["title"]))
                    .replace("__ACCENT__", deck.get("accent", "#7aa2ff"))
                    .replace("__DECK__", data))
        Path(argv[2]).write_text(page, encoding="utf-8", newline="\n")
        print("wrote", argv[2])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
