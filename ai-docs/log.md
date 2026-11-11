# Log

## 2026-11-10 (session 4)
- Son's first natural-selection run: 67% first try, streak 7; missed faster (sexual repro), variation first step, populations, generations, which snails are seen, fitness=reproduce, mutation, genetic variation. Recorded in records/natural-selection/2026-11-10-run1.* (screenshot, no typed answers).
- Built follow-up deck natural-selection-2 (22 q, new scenarios: deer fitness, clones and disease, fish A/B, rabbits, moths, giraffes, bacteria, beetles, finches, pesticide).
- Engine 0.3.0: hero/classes/feats/study areas, character sheet with past games, JSON record download per game, sw.py records. Play-tested in Chrome by script: full run, Keen Eye, two level-up picks, record saved, sheet lists the game. No JS errors.
- records/ gitignored because the repo is public and records are a child's results.

## 2026-11-10 (session 3)
- README banner: Z-Image Turbo 1536x640 on the Mac, four seeds, picked seed 2313760545 (only take with no fake lettering on the worksheet). Workflow and prompt in .github/images. PR #1 merged. Discussions enabled.
- Social preview crop not uploaded (no API).

## 2026-11-10 (session 2)
- Mark: row 4 name is Barr (deck changed from Baron de Bastrop; Barr explained as an Irish-born Nacogdoches trader working with Spain, still NO).
- Added 28 questions from the "Louisiana Purchase and Father Hidalgo" study guide. Student blanks taught correctly: 13 colonies blank is the year 1776; Rubi kept San Antonio and La Bahia (sheet had "Texas"); purchase about $15 million; Hidalgo a Catholic priest, Grito de Dolores 1810; fled north (not to Guadalajara) before capture.
- Mark asked for a PUBLIC repo with wiki and the plugin installed.

## 2026-11-10
- Made from three worksheet photos (son's Texas history filibuster sheet; science 4.7 notes + natural selection sheet).
- Built games/texas-filibusters.html (19 q) and games/natural-selection.html (24 q); both played through in Chrome: right/wrong + why, requeue of misses, review list, three.js tower all working.
- Guesses: Texas row 4 printed name was overwritten "Barr"; read as Baron de Bastrop (fits the checks: foreigner, land, gain, no fight). Jean Lafitte kept as filibuster per worksheet.
- Student answers noted wrong on the science notes: "Only ___ variation" should be **genetic**; "favors the ___" should be **survival**; "developed" for evolution blank. Games teach the correct ones.
- Everscout beat learning-games created at ~/.everscout/beats/learning-games (not scanned yet).
- No GitHub repo made yet (needs Mark's ok; private, child's schoolwork).

## 2026-11-10 session 5
Mark: biology test done; update Texas game to latest engine; questions should show the hero overcoming tasks, each subject a realm; Start quest should offer continue / other / new hero. Built 0.4.0 in game.html (REALMS table, chal(), pickHero), added `realm` to decks, rebuilt games, play-tested in Chrome on 127.0.0.1:8791 (test hero removed). Note: port 8765 was taken by another server.

## 2026-11-10 session 6
- Texas game not played yet (sw.py records: nothing new).
- Engine 0.5.0: day-2 warm-up (per-deck `miss` list + `last` local date in the deck key; next run queues misses first, title shows a warm-up line) and read-aloud button (speechSynthesis, reads the visible choices in shuffled order). All three games rebuilt. Scripted play-test in Chrome on 127.0.0.1:8791: 2 misses saved and queued first, warm-up text shown, button present, no errors; test hero and keys removed.

## 2026-11-10 session 7
- Texas game still not played (sw.py records: nothing new).
- Engine: boss round (timed pass over first-try misses after the main run; bonus XP; `boss` field in the record; skip button). Games rebuilt. Scripted Chrome play-test on 127.0.0.1:8791: intro, timer bar, timeout counts as a miss, finish screen boss line, record field; no JS errors; test hero removed (localStorage restored).

## 2026-11-10 session 8
- Texas game still not played (sw.py records: nothing new).
- Engine: two-player hot-seat (duoPick, startDuo, duoTurn; per-hero tally in S.duo.p; record `duo`; the partner gets a record copy and a quest count; World.tint recolors the 3D hero each turn). Finish line says "The team earned" in duo mode.
- Scripted Chrome play-test on 127.0.0.1:8791: turns alternate A,B,A,B; scoreboard and boss shown; 2 records (one per hero); 1 download; no JS errors; localStorage restored.
- Version 0.6.0 (covers 0.5.0 warm-up/read-aloud, boss round, hot-seat).

## [2026-11-11] docs | Works with section
README gained a Works with section (ludowright, everscout, askwright); the wiki gained a Works-with page linked from the sidebar and Home. Each entry describes a handoff found in the skill files on one side or the other.
