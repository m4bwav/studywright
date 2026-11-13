# studywright

Plugin that turns worksheets into study games, and the knowledge base on how to build learning games (techniques, research, learning design). Skill: [skills/studywright/SKILL.md](skills/studywright/SKILL.md).

- Engines: `skills/studywright/templates/game.html` (quest: one page, deck JSON injected, three.js r128 from cdnjs, works without it) and `templates/lesson.html` (teach a method, `mode: "lesson"`). `templates/kit.js` is injected into both by `sw.py build` (hero drawing, hero builder, notes prompt): change hero looks there, then rebuild every game.
- The open-world study RPG (world mode, the decks from schoolwork, the built games and the study records) moved to its own private repo on 2026-11-12: `D:/m4bwa/Claude/Projects/Ai/studyquest` (m4bwav/studyquest). Work on that game happens there. What it teaches about learning games comes back here as notes in `references/learning-design.md` and `RESEARCH.md`.
- Every mode must end a play with a downloaded log and the notes prompt (`Kit.notesHtml`).
- CLI: `python skills/studywright/scripts/sw.py check|build DECK.json [OUT.html]` (stdlib only).
- Decks here are samples only: `skills/studywright/decks/sample-*.json`. Built samples: `games/`.
- State and next steps: [ai-docs/HANDOFF.md](ai-docs/HANDOFF.md). Log: [ai-docs/log.md](ai-docs/log.md).
- This repo is public: no deck, photo or record from a child's schoolwork goes in it, and no child's name in any file.
