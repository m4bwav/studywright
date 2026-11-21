# Changelog

## 0.21.0 (2026-11-21)
- `sw.py check` (new `check_reuse`): WARN MISCONCEPTION-ONCE when a `mis` tag sits on fewer than 3 items (variants count); ERROR on a `pair` id used once, WARN when a math or science deck of 20+ items has no pair; ERROR on a malformed `why`, WARN KEY-NO-WHY when a topic of 5+ items has no `why`; WARN when a science deck of 15+ items has no predict item. `scripts/test_sw_reuse.py`, 7 tests (each check fires on a bad case, quiet on a good one); suite 37 passed. Samples stay warning-free.
- game.html: `why` follow-up after a right pick (mastered only when the reason is right; a wrong reason requeues the item and adds it to `lucky_guesses` in the record). The single debrief line became the three exam-wrapper questions; the notes prompt lists lucky guesses and asks for the answers as `wrapper`. `sw.py records` prints both.
- because: Ambrose et al., How Learning Works (ch. 1, 4, 7); Zinsser, Writing to Learn (ch. 11). Dropped: see the PR body.

## 0.20.1 (2026-11-21)
- `sw.py check`: WARN once per term that another deck in the same folder defines in its glossary, this deck's lesson or quiz text uses (accepted answers and ids skipped), and this deck's glossary lacks; names the deck that defines it. Same matcher as the word cards (longest phrase up to 4 words, plural fallback, aliases). Unreadable sibling files are skipped. 3 new tests in `test_sw_glossary.py` (positive, negative, alias and plural); suite 30 passed.

## 0.20.0 (2026-11-21)
- Deck `glossary` (`term`, `def`, `plain`, optional `aliases`): `sw.py build` injects `templates/glossary.js` (only when a deck has one), which marks glossary words in all lesson and quiz text, including text the game adds later, and shows a word card on hover, tap or keyboard focus. Longest phrase up to 4 words wins; a word ending in s falls back to the singular. Card at most 300 px wide, above the word with room, else below, kept 8 px inside the screen; no dialog. A corner button switches "Plain, easier to read" (default) and "Original, as written", saved in localStorage, the open card re-renders at once; plain falls back to def. Fade off under prefers-reduced-motion.
- `sw.py check`: ERROR on a glossary entry with no `plain` or no `def`; WARN when `plain` is longer than `def` and on duplicate terms or aliases. Lesson decks are checked too.
- Sample deck states-of-matter has a 4-word glossary. Built page 75,998 to 82,130 bytes; headless Chrome probe: 3 words marked (plural and 3-word phrase), card opens on focus, stays inside the screen, flips below at the top edge, switches register live, saves it, no errors.
- `scripts/test_sw_glossary.py`, 6 tests (match logic, check rules, and the JS matcher run under node against the same cases).
- because: technique harvest, a browser game's common room (second register for hard words, read in place).

## 0.19.0 (2026-11-20)
- `verify_xp.py`: warns when an easier choice the child can make pays more XP per minute than a harder one (`--rates TABLE.json`, or a built-in game.html table read from its award line). On game.html: 1 warning (replaying a mastered deck about 150 XP/min vs 47 for a new deck, time and accuracy guessed); on a studyquest table: 0 of 2 groups (review 54 vs new 50 XP/min, under the 10% tolerance). Rate warnings never fail the run. 4 new tests in `test_verify_xp.py`.
- `sw.py names [FILE ...]`: lints feat, badge and title names in engine files for trait praise and mocking words; `sw.py check` also lints a deck's optional `feats`, `badges`, `titles`. 0 warnings over 35 names in the templates and 51 in studyquest's engine (no false positives). `scripts/test_sw_names.py`, 4 tests.
- learning-design.md: easy-picks-must-not-pay-better line; reward names, two voices and feedback faded by mastery (the last two as small studies to test with the child first).
- because: Kapp, The Gamification of Learning and Instruction (ch. 4, 10), second pass. Leaderboard caution not added: the no-leaderboard line already stands.

## 0.18.1 (2026-11-20)
- learning-design.md: help ladder keyed to miss count (presets 0/2/4 and 3/5/7), measured warning against immediate retries (47% echo under a 50% random draw), 2.2 s miss hold and 1.2 s advance gate after praise, mixed-age co-play idle hints (9-13 s and 30 s).
- because: an open-source kids' word game played headless and timed (technique harvest, web games 2026-11).

## 0.18.0 (2026-11-19)
- learning-design.md: illusions of knowing (optional sure/guess with sure-and-wrong listed first), end-of-round re-ask, try-first and one-line rule in lessons, two surface forms and which-method items, cumulative follow-ups, Leitner level per item, effort praise, no false premise, too-easy lessons. SKILL.md: cumulative follow-ups, no-false-premise and praise rules.
- `sw.py check`: warns on trait praise ("smart", "genius", "gifted", "clever", "brilliant", "a natural") in `win`/`explain`/`scene`/`intro`/`practice` (`scripts/test_sw_praise.py`, 2 tests). Fires on neither sample deck nor any template.
- because: Brown, Roediger, McDaniel, Make It Stick (ch. 1-8); book rules, unverified, except the praise check.
- learning-design.md: encoding aids for bare facts and lists (hook after a first miss, vivid child-safe images, concrete stand-ins, route lesson, gist before verbatim, pattern before sequence) and speed rounds against the child's own best with a hard-ones round.
- `sw.py check`: optional per-question `hook`; fails on a non-string hook, warns on 5+ typed items with no hook (`scripts/test_sw_hooks.py`, 4 tests). Fires on neither sample deck.
- because: Foer, Moonwalking with Einstein (ch. 2, 3, 5, 6, 8); book rules, unverified, except the hook check.

## 0.17.1 (2026-11-19)
- learning-design.md: homework-night short form (about 10 warm-ups on new numbers, one per step the sheet uses; solve the sheet first and check it against its answer key; figures stated in words in finale items).
- because: studyquest Scorpion Desert (exterior angles), one child playtester.

## 0.17.0 (2026-11-18)
- learning-design.md: homework finale (worksheet problems as `homework: true` boss questions after mastery, graded by hash, misses reveal nothing) and showing every number as its sum.
- because: studyquest homework quest and list 3 play-test work (one child playtester; unverified beyond that game).

## 0.16.0 (2026-11-14)
- learning-design.md: per-topic mastery as a retention bar that drains without review, rewards that taper on repeats of mastered items (variable-ratio ban kept), optional child-written questions checked by an adult before entering a deck.
- because: Ferro, Gamification with Unity 5.x (ch. 1, 10); book rules, unverified.

## 0.15.0 (2026-11-14)
- learning-design.md: observe, assess, respond table; a misconception note per wrong choice; difficulty changes between sessions only, never mid-quiz; a check pass for AI-written questions and a search when a sheet fact changes.
- `sw.py check`: optional deck key `objectives` and per-question `objective`; fails when a goal has no question or a question names an unknown goal (`scripts/test_sw_objectives.py`, 5 tests). No current deck uses the key, so it fired 0 times on the 2 samples and 7 studyquest decks.
- because: Mangos and Ferraro (eds.), AI and Gamification Technologies for Complex Work Simulation and Training (ch. 3, 6, 7). Adult workplace and military training; child use unverified. Book rules, unverified, except the coverage check.

## 0.14.0 (2026-11-13)
- learning-design.md: consent and pausing without penalty, a finish state per topic arc, never devaluing earned rewards, a sink for every currency, the same-task rule, a weakest-player check for competition, a loophole pass before shipping a reward.
- because: Brian Burke, Gamify (ch. 7-8); book rules, unverified.

## 0.13.0 (2026-11-13)
- `scripts/verify_xp.py` (+ `test_verify_xp.py`): fails if a template lowers or overwrites XP, pays gold from XP or buys XP with gold. Current templates: 0 breaks.
- learning-design.md: XP vs gold, progress bars that always show the next tier, an optional weekly XP window (not built), no leaderboards.
- because: Zichermann and Cunningham, Gamification by Design (ch. 3); bar and weekly-window rules are book rules, unverified.

## 0.12.0 (2026-11-13)
- learning-design.md: content type to question form table, a multiple-choice item checklist, pre-brief and debrief, the delayed retest as the honest learning signal, named failures (pointsification, badge inflation, rewards crowding out interest, no variable-ratio rewards or scarcity timers for kids, a rewards-off playtest), and two ideas not built (co-play, a lesson note for the parent).
- `sw.py check` prints WARN lines (never failing) for a choice much longer than the others and for "all/none of the above".
- Quest games: optional deck key `practice` shows a "Today you'll practice" line on the title screen; the finish screen shows a skill word beside the score and asks one debrief question.

## 0.11.0 (2026-11-12)
- The open-world study RPG moved out to its own game, studyquest, to grow by itself. Removed from the plugin: `templates/world.html`, world deck checks in `sw.py`, the `order` question type and question pictures (both were world-only), and `juice-changes.md`.
- `sw.py check` now rejects a deck with `mode: "world"` and says where it went. Quest and lesson decks build as before.
- The decks written from one student's schoolwork and their built games left the repo. Two samples replace them: `decks/sample-states-of-matter.json` (quest, written from scratch) and `decks/sample-mean-absolute-deviation.json` (lesson).
- The plugin keeps the quiz and lesson builders, the shared hero kit, the paper trail, the research and the learning-design notes.

## 0.10.0 (2026-11-12)
- World mode: merchants. A region with `merchant` gets a trader who sells a healing potion (drunk by itself at zero hearts), a trail map of the valley, a compass (HUD arrow and step count to the nearest waiting creature) and up to four deck-written keepsakes that each show a fact from the notes when bought. Gold finally has a use; nothing sold answers or skips a question.
- The record carries `bought` and `gold`; `sw.py records` lists the purchases; `sw.py check` validates `merchant`.
- A Ranger's starting compass now works in world mode. A hero's starting potion is used at zero hearts.
- Fix: the heart count in the HUD stayed at 0 after waking at camp until the next answer.
- Deck texas-independence: a merchant in each of the 8 regions, 15 keepsakes.

## 0.9.0 (2026-11-12)
- World mode: `type: "order"` questions (tap the items first to last, undo, each item marked right or wrong) for timelines and processes.
- World mode: pictures on a question (`figs` in the deck, `fig` and `hl` on the question): an inline SVG with one shape lit up, for label-the-map items.
- Fix: a creature could be placed in a pocket closed off by other creatures and never be reached. Placement now skips a cell that would cut any creature off. Decks that were fine keep their layout.
- New deck texas-independence ("Texas Frontier", 90 q, 8 regions): Mexican independence, filibusters, empresarios, a map of 1803, a timeline tower, vocabulary and a review region for the earlier sheets.
- sw.py check: validates `order` items and `fig` names.

## 0.8.0 (2026-11-12)
- World mode (`mode: "world"`, templates/world.html): an open world on a canvas. Walk in four directions; water, mountains, trees, walls and locked doors block. Regions with signpost notes, a creature per question, keys for mastered regions, a locked hall with the final chest. The land, its fog and its buildings are shared by every world game and persist between plays.
- templates/kit.js, injected into every template: one hero drawing routine (map, HUD, title, builder), a hero builder with explanations and new options (hat, cape, face, three more hair styles, two more hair colours, three more outfits, five more companions, a random button), and the notes prompt.
- Every finish screen in every mode now shows a notes prompt with a copy button next to the saved log.
- Lesson mode (templates/lesson.html, not released before): worked example, faded steps, solo, generated numbers; now with the hero picker and builder it lacked.
- Sound effects in world mode (steps, bumps, coins, keys, doors, builds, level-ups), synthesized in the page; feel settings in the gear menu.
- New deck selective-breeding ("Breeders' Valley", 45 q): selective breeding, genes and traits, with a review region for natural selection and reproduction.
- sw.py: checks and builds world decks; records notes what was not reached and the route.

## 0.7.0 (2026-11-11)
- Read lock, question variants and steps, hero scenes with hp/gold/loot, hero builder with inventory; deck natural-selection-3.

## 0.6.0 (2026-11-10)
- Two-player hot-seat: "Two players" on Start quest picks two heroes who take turns, one question each. Each hero keeps its own XP, feats and level-ups; the finish screen shows a team scoreboard; the record carries `duo` and is filed under both heroes.
- Boss round: a timed pass over the first-try misses after the main run (+15 XP per hit, skippable; `boss` in the record).
- Day-2 warm-up (last run's misses come first) and a read-aloud button (0.5.0, not released separately).

## 0.4.0 (2026-11-10)
- Realms: each subject is a themed 3D world (props, sky, obstacle); each question is a challenge the hero overcomes, with win/lose lines.
- 3D hero stands on the tower and leaps up as obstacles shatter.
- Start quest asks: continue as the last hero, pick another, or start a new one.
- Rebuilt all three games; decks carry `realm`.

## 0.3.0 (2026-11-10)
- Persistent hero shared by every game in the browser: name + class (Scholar, Ranger, Knight, Mage, each with a starting feat), switch or add heroes, load a hero from a saved record.
- Level-ups (XP curve 100, 300, 600...) offer a choice: +1 training in the deck's study area, or a feat (Keen Eye, Second Wind, Scribe, Grit, Battle Focus, Sage of an area at level 3). Study areas also rise by use, every 15 right answers.
- Character sheet: study areas, feats, and every past game with scores, missed topics and a link to the game.
- Paper trail: each finished game saves studywright-<deck>-<time>.json to Downloads (and keeps the last 200 in the browser); `sw.py records` files them into records/<deck>/ as JSON + Markdown with records/INDEX.md. records/ is gitignored (a child's results).
- Decks take optional `stat` (study area; default the subject before the colon) and `follows` (the deck this one re-tests).
- New deck natural-selection-2 (22 q): follow-up check on the 8 first-try misses of the first run, all in new scenarios.

## 0.2.0 (2026-11-10)
- Texas deck becomes "Texas Test Prep" (47 q): Seven Years War, Rubi, 1776, Louisiana Purchase, Father Hidalgo, timeline order, from a second study guide.
- Row 4 is Barr (confirmed), not Baron de Bastrop.

## 0.1.0 (2026-11-10)
- Engine, sw.py check/build, two decks (Texas filibusters, natural selection).

## 0.16.1 (2026-11-15)
- SKILL.md: multi-handout units go to studyquest world decks; length-clue rule (41/103 drafts gave the answer away); patterns for flashcards, short answer + rubric, tiers, spiral review src, stretch items; frontmatter version caught up (said 0.15.0 after 0.16.0).
