# studywright

Plugin that turns worksheets into study games. Skill: [skills/studywright/SKILL.md](skills/studywright/SKILL.md).

- Engine: `skills/studywright/templates/game.html` (one page, deck JSON injected, three.js r128 from cdnjs, works without it).
- CLI: `python skills/studywright/scripts/sw.py check|build DECK.json [OUT.html]` (stdlib only).
- Decks: `skills/studywright/decks/*.json`. Built games: `games/` (open the .html directly in a browser).
- State and next steps: [ai-docs/HANDOFF.md](ai-docs/HANDOFF.md). Log: [ai-docs/log.md](ai-docs/log.md).
- Private repo material: decks come from a child's schoolwork; keep the child's name out of every file.
