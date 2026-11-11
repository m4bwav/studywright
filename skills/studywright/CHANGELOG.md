# Changelog

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
