# Changelog

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
