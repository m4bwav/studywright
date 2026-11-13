---
name: studywright
description: "Turn a student's worksheets, notes or study guide (photos, PDFs or text) into a playable study game: one offline HTML page that quizzes every item on the sheet, says right or wrong and why after each answer, brings misses back until mastered, and adds game elements (XP, levels, streaks, a three.js tower that grows with right answers, end-of-game review list). Use on 'make a study guide game', 'quiz my kid on this worksheet', 'turn these notes into a practice test', 'study game for the science test', 'flashcard game from this'. Also 'refresh studywright'. Not for grading finished work or for designing a commercial game (ludowright)."
license: MIT
metadata:
  version: "0.3.0"
---

# studywright

You make study games that teach, not just test. Read [evergreen.json](evergreen.json) with this file; if today is past `next_due`, say so in one line, do the task, then refresh against [RESEARCH.md](RESEARCH.md).

The engine is [templates/game.html](templates/game.html); `SW build` fills it. `SW` means `python "<this folder>/scripts/sw.py"`. Run it; do not read it.

## Steps

1. **Read the sheets.** Photos are often rotated: read every blank, table row and example. Where the student filled blanks in, use them only as hints; work out the correct answer yourself and note any the student got wrong (tell the parent). Where a printed word is illegible, infer from the subject and record the guess in the project log.
2. **Write one deck per test** as JSON in `decks/<slug>.json` (format below). Coverage rules:
   - every blank, every table row and every worked example becomes at least one question; key ideas get two (one recall, one apply/why);
   - mix `mc` and `type` (typed recall is stronger practice; keep typed answers to one or two words and list spelling variants in `accept`);
   - wrong choices must be plausible misconceptions (e.g. "organisms choose to change"), not jokes;
   - every question has `explain`: why the right answer is right, in one or two sentences a 12-year-old reads easily; for classify-the-row questions, name the criterion that decides it;
   - optional `review`: a short label for the end-of-game review list;
   - 15 to 25 questions per test; group by `topic` using the sheet's own headings.
3. **Build and check**: `SW build decks/<slug>.json games/<slug>.html`. Fix every ERROR.
4. **Play it through** in a browser (serve `games/` on 127.0.0.1 if file:// is blocked; port 8765 may be refused on Windows, use 18765): answer some wrong, confirm the miss returns and the end screen lists it with its answer.
5. **Follow-up tests.** Before writing one, read `records/INDEX.md` and the linked records (run `SW records` first to file new downloads). Write a new deck with `"follows": "<old id>"` that re-tests every first-try miss at least twice in NEW scenarios (apply it, not recall the sheet's wording), plus a few items the student got right as a check.
6. Hand over each game so the parent never has to select text: put its URL (`file:///D:/path/to/games/<slug>.html`, forward slashes, spaces as %20) on the clipboard yourself (`Set-Clipboard '<url>'` on Windows, `pbcopy` on macOS, `xclip -sel c` on Linux) and say "the link is on your clipboard, paste it into the browser"; also give a clickable markdown link and the URL on a line of its own in a code span. A code span alone failed (2026-11-12): in the VS Code chat panel a long path wraps and cannot be selected and copied. The pages work offline (three.js is optional, the quiz runs without it).

## Deck format

```json
{"id":"slug","title":"Game name","subject":"Class: unit","accent":"#4cc9f0","intro":"one line",
 "questions":[
  {"topic":"Vocabulary","q":"Fitness is the ability to survive and ______.","type":"type","accept":["reproduce","reproduction"],"explain":"..."},
  {"topic":"People","q":"Moses Austin: filibuster or not?","choices":["Filibuster","Not a filibuster"],"answer":1,"explain":"...","review":"Austin asked permission"}]}
```

Optional deck keys: `realm` (history, biology, math, science, words or quest; guessed from the subject if missing: each subject is a themed 3D world and every question opens with a challenge the hero overcomes), per-question `scene`/`win`/`lose` (custom challenge text; `{h}` = hero name, `{t}` = topic), `variants` (list of rewordings of the same idea, each a full mc or type item; a miss comes back in the next wording), `steps` (2-3 smaller sub-questions asked right after the first miss, before the full question returns; use them for every key idea), `foe` (emoji shown in the scene), `stat` (the hero study area this deck trains; default is the subject before the colon) and `follows` (id of the deck this one re-tests).

`type` defaults to `mc`; choices are shuffled at play time, `answer` indexes the list as written.

Every main question should carry at least one `variant`; key ideas also get `steps`. The engine locks Next for 3 seconds after each answer so the reason gets read, shows a scene of the hero against the foe (gold, loot and hearts on a right answer; damage or dropped gold on a miss; fainting only sends the hero back to camp), and the hero builder (class, weapon, skin, hair, outfit, pet) draws a unique hero with an inventory.

## Lesson mode (teach a new method)

A deck with `"mode": "lesson"` builds from `templates/lesson.html`: worked example, then faded steps, then solo, with generated numbers, named slips and a path map; it needs `skills`, `map` (stages naming an encounter kind), `contexts`, `gold` and optional `banned_hashes`. Example: `decks/mean-absolute-deviation.json`. Before handing it over run `node scripts/verify_lesson.js games/<slug>.html 3000 [banned-sets.json]` and `python scripts/verify_routes.py <deck>`.

## Learning design (why the engine works this way)

See [references/learning-design.md](references/learning-design.md). In short: retrieval practice beats rereading; feedback right after each answer with the reason; misses come back a few items later (spacing) until answered right (mastery); no lives or game over, so a miss costs only the streak; rewards follow correct effort (XP, streak gold, tower) and never block learning. A persistent hero (class, levels, feats, study areas that rise by use and by training picks) carries across games; feats only add XP or one strike-out hint, never skip questions.

## Paper trail

Every finished game downloads `studywright-<deck>-<time>.json` (hero snapshot, score, each first-try miss with what was typed). `SW records [--from DIR] [--to DIR]` files them into `records/<deck>/` as JSON + Markdown and rebuilds `records/INDEX.md`. Agents read INDEX.md before writing the next test. Keep records out of public repos (gitignored here).
