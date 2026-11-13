# studywright

Plugin that turns worksheets into study games. Skill: [skills/studywright/SKILL.md](skills/studywright/SKILL.md).

- Engine: `skills/studywright/templates/game.html` (one page, deck JSON injected, three.js r128 from cdnjs, works without it).
- Other engines: `templates/world.html` (open world, deck `mode: "world"`, the default for a test) and `templates/lesson.html` (teach a method, `mode: "lesson"`). `templates/kit.js` is injected into all three by `sw.py build` (hero drawing, hero builder, notes prompt): change hero looks there, then rebuild every game.
- World decks also take `type: "order"` questions and SVG pictures (`figs`, `fig`, `hl`); see the skill's World mode section.
- Every mode must end a play with a downloaded log and the notes prompt (`Kit.notesHtml`).
- CLI: `python skills/studywright/scripts/sw.py check|build DECK.json [OUT.html]` (stdlib only).
- Decks: `skills/studywright/decks/*.json`. Built games: `games/` (open the .html directly in a browser).
- State and next steps: [ai-docs/HANDOFF.md](ai-docs/HANDOFF.md). Log: [ai-docs/log.md](ai-docs/log.md).
- Study records (paper trail): `records/INDEX.md`, filled by `sw.py records` from the JSON each game saves to Downloads; gitignored. Read it before writing a follow-up deck.
- Private repo material: decks come from a child's schoolwork; keep the child's name out of every file.
