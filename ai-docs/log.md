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
- Version 0.6.0 (covers 0.5.0 warm-up/read-aloud, boss round, hot-seat).

## 2026-11-11 session 9
- Mark asked: 3 s read lock after each answer, question variants and step-downs after a miss, hero scenes with damage/gold/loot, unique-looking builds with inventory, and a new test from "How Natural Selection Works" to Key Takeaways (son's sheet photo, all his blanks correct: variation, population, asexual, sexual, reproduction, mixing, faster, higher, diversity, mistakes, populations, generations).
- Engine 0.7.0: READ_SECS lock (Next disabled with countdown, Enter blocked); queue entries can be {p,s} steps; itemOf picks variants by ask count; outcome() hp/gold/loot/potion/faint (no game over); SVG avatar() from hero.look; heroCreate builder; 3D hero dressed from look; old heroes migrated by fixHero.
- sw.py check validates variants and steps.
- New deck natural-selection-3 "Wilds of Selection" (18 q, every q has variants, most have steps). Chrome play-test on 127.0.0.1:18765: miss queued 2 steps, lock held 3 s, variant shown on return, inventory/gold/hp change.

## 2026-11-12 prompt | lesson mode kickoff
- Mark asked for a prompt, not a build: grow studywright so it can teach a method (his son is stuck on the first questions of HW 5.6, Mean Absolute Deviation Part II, due 2026-11-13), in a game of ten minutes at most that prepares him for the worksheet without doing it, with a roguelike choice of paths on a map after each encounter, then a ludowright round and a game-juice round.
- Written: ai-docs/plans/2026-11-12-lesson-mode-kickoff-prompt.md. It ends by handing back to the standing continue prompt.
- Worksheet photo copied to records/mean-absolute-deviation/hw-5.6.png with a transcription, number profile and answer key in worksheet.md beside it (gitignored; the repo is public, so nothing from the sheet goes in a deck).
- Rulings made in the prompt, for Mark to overrule: the first link goes out before the ludowright and juice rounds; every map route teaches all five skills and has the same length; a miss gets one retry with new numbers and then the run moves on, so the ten minutes hold; procedure questions draw generated numbers.
- Nothing committed; the prompt, this entry and the HANDOFF edit are uncommitted on main for the build session to carry onto its branch.

## 2026-11-12 session 10 | lesson mode, first link
- Built lesson mode as a separate template (templates/lesson.html), chosen by deck `mode: "lesson"`; the four quiz games rebuild byte-identical. sw.py check_lesson validates skills/map/contexts/gold, refuses raw `banned` sets (worksheet sets live only as FNV-1a hashes in `banned_hashes`).
- Engine: number boxes (7.6, 7.60, " 7.6", ".5" accepted), generated five-value sets with whole means, slip naming (mean, undivided sum, 0 from signs, /4, /6; mean slips sum, median, /4), dot plots with mean line and distance bars, worked steps after a miss, one retry with new numbers (none after 8:00), path map (Camp = help +10 gold, Lair = no help, bigger numbers +25), level-ups deferred to quest games.
- Time budget: intro 0.5 min, mean 1.5, spread 0.5, worked MAD + faded 1.5, whole MAD 2.5, read 0.75, both 0.75 = 8 min; retries cut off at 8:00 so a run stays near 10.
- Verified: verify_lesson.js 3000 runs x 6 kinds x 2 paths (54000 items): profile, keys against independent maths, slips never equal the key, no worksheet set (raw list in gitignored records/.../banned-sets.json). verify_routes.py: 64 routes, all 6 stages, all 5 skills. Chrome play-test on 127.0.0.1:18765: clean answers, odd number forms, each MAD slip named, wrong MC why, end screen, record (elapsed_sec, route, per-skill first_try). Hero Zed's state and records restored by hand; test download deleted. The first check found a bad slip (a positive distance flagged as the negative-sign slip); fixed.
- Small rulings: separate template rather than branching game.html (zero risk to the old decks); encounter kinds live in the engine (KINDS) and decks name them; the path choice is help-vs-gold on every stage, as the prompt suggested, not yet judged by ludowright.
- Wrap-up 2026-11-12: SKILL.md step 6 now puts handover URLs on the clipboard (Mark could not copy a code span in the VS Code panel); SKILL.md gained a Lesson mode section naming lesson.html and the two verifiers.

## 2026-11-12 session 11 | world mode, shared hero kit, biology test game
- Mark: lesson mode lost the character options and needed more variation and explanation; every play must create a log and a prompt to update the notes; the main game should be an open world (four directions, blocked by locked doors, walls, mountains), mapped and developed from game to game, with characters consistent between plays; biology test 2026-11-13 on a selective breeding guide plus the 4.9 genes sheet, also testing this week's natural selection and reproduction; better avatar and options, game-juice, sound.
- Built templates/world.html (2D canvas, one offline file): seeded terrain, a valley per deck stamped on one shared land (studywright:world: fog bitmaps per 16x16 chunk, buildings with levels, opened chests, found regions, deck origins), regions on a ring around the hub with roads, walled regions with key doors, signpost notes, a creature per question, cool-down then a reworded retry after a miss, keys per mastered region, hall chest ends the quest, resume of an unfinished quest, map screen, WebAudio sounds, feel settings (juice-changes.md).
- Built templates/kit.js and injected it into game.html, lesson.html and world.html: drawHero (canvas), builder (hat, cape, face, more hair, outfits and companions, random button, a line of explanation per option), notesPrompt/notesHtml. game.html's avatar() now returns the kit image; its old SVG avatar and builder are kept as avatarSvg/heroCreateOld, unused.
- Deck selective-breeding: 7 regions (farm hub, ranch, kennel, mill, ridge = review, lab locked 1 key, hall locked 4 keys), 45 questions, variants on the main-sheet items. Both sheets read as correctly filled in; nothing to tell the parent.
- Verified: sw.py build of all six decks; Chrome on 127.0.0.1:18766 (a clean origin, cleared afterwards): BFS reaches all 45 sites, 7 signposts, camp and chest; a miss costs a heart, blocks the retry until another answer, returns as the variant; typo "humansx" accepted; farm key earned; lab opens with 1 key, hall refuses with 1 and opens with 6; chest sealed until the hall is cleared, then finish downloads the log and shows the prompt; reload keeps the map and the buildings; quest and lesson pages show the kit hero, builder and prompt with no JS errors. verify_lesson.js 54000 items ok (its DOM stub now supplies a hero; Kit.img returns '' when canvas is missing); verify_routes ok.
- Small rulings: 2D canvas rather than three.js (must work offline from one file the night before a test); world decks keep `variants` but not `steps` yet; gold has no use yet; an early finish scores only what was asked and lists the rest as not reached; filenames keep the UTC stamp the other modes use.
- Not done: lesson mode variation and explanation (HANDOFF 01).

## 2026-11-12 session 12 | Texas Frontier world deck, order questions, map pictures
- Mark: final study guide for the Texas history test of 2026-11-13 (six photographed pages, filled in by the son); make a game in the same world as the biology one, focused on the guide plus the week's other Texas material, with a new feature.
- Deck skills/studywright/decks/texas-independence.json, world mode, 90 q: Dolores Plaza (hub, Part 2 Hidalgo, 14), Big Picture Mesa (Part 1 + the 1803 map, 13), Filibuster Trail (Part 3, 11), Austin's Colony (Part 4, 12), Word Mill (Part 7, 12), Old Camino Real (review of the earlier sheets, 10), Clock Tower (Part 6 timeline, walled, 2 keys, 7), Hall of the Republic (Part 5 compare + apply, walled, 5 keys, 11). Generated once by a script; the JSON is the source now.
- New in world.html: `type: "order"` (tap first to last, undo, per-item right/wrong), `figs`/`fig`/`hl` (inline SVG with one lit shape; variants inherit, `hl: ""` shows it unlit), ansOf for order. sw.py checks both.
- Bug found by the play-test: 89 of 90 creatures reachable. Sites sit on a checkerboard, and three creatures can close a corner pocket around a fourth. Fix: placement skips a cell if any creature would lose its last open neighbour (flood-fill from the region centre). selective-breeding's 45 positions are identical before and after (compared in the page), so buildings already saved in a browser still line up.
- Verified in Chrome on 127.0.0.1:18767 (clean origin, cleared after): 90 of 90 reachable, 8 signposts; order right, order wrong with undo (retry blocked until another answer), map question lights region 2, its variant shows the map unlit, all 90 answered gives 7 keys and a record with the one planted miss. The finish download was not run again (unchanged code).
- Sheet reading (details in records/texas-independence/study-guide-notes.md, gitignored): wrong on the sheet were Q2 (wrote France; Great Britain), Q3 (wrote America; Spain), map region 2 (wrote France; British North America), Q41 left blank (11 years); Hidalgo's birth year is hard to read (1753 is right). The deck doubles up on those.
- Small rulings: Samuel Kemper left out (the son wrote NO, he was a filibuster historically, class key unknown); "Father of Mexican Independence" as on this guide (the older deck says Father of the Nation); settler reasons taken as cheap land and escaping debt; 90 questions is long for one evening, the Finish button logs what was not reached; order and pictures are world-only (game.html unchanged).
- Not done: evergreen-refresh of the due units; wiki update.

## 2026-11-12 session 13 | first Breeders' Valley play filed
- Mark pasted the notes prompt from the finish screen: selective-breeding, world mode, finished 2026-11-13 03:16 UTC, 29 min, 80% first try (36/45), 45 of 45 mastered, nothing unreached, signposts read: all but the mill.
- The log file studywright-selective-breeding-2026-11-13-03-16.json was not in C:\Users\m4bwa\Downloads (no studywright-*.json there at all), so the record was written by hand from the pasted results: records/selective-breeding/2026-11-13-03-16.json and .md (gitignored). If the real file turns up, `sw.py records` skips it because that name exists; delete the hand-written pair first to take the full log.
- Missed first try (9): naturally; more milk; large eggs; step 2 parents (typed "best"); hip dysplasia picture (chose "always makes animals healthier"); Baby Z parents (chose speed + shapeshifting); genes (typed "tratis"); genetic variation (typed "trait"); true-for-both (chose "makes more genetic variation every time"). All right on the retry.
- Reading (agent's interpretation): trait/gene/variation vocabulary is the shakiest idea and repeats a 2026-11-10 miss; the downside of selective breeding (less variation, health problems) is second; step 2 against step 3 third; the three wording blanks and Baby Z look like guesses or slips. Re-test plan is in HANDOFF and in the record.
- Bug fixed: `sw.py records` raised TypeError rebuilding INDEX.md because records/mean-absolute-deviation/banned-sets.json is a list, not a record. The index loop now skips JSON that is not a dict with `studywright_record`. Checked by running it: 2 records listed.
- Not done: no follow-up deck built (the test is 2026-11-13; waits on Mark asking); why the download was missing is unknown.

## 2026-11-12 session 14 | merchants in world mode (0.10.0)
- Mark: before the son plays, add merchants to the Texas history game.
- world.html: region key `merchant` (true or {name, icon, hello, goods}); the trader is placed on the free cell nearest the region centre after all creatures, through the same walled-in check, so creature positions do not change. Tile `M`, shop card, purchases in `S.bought`, record fields `bought` and `gold`, a line in How to play.
- Goods: healing potion (10 gold; at zero hearts it is used and the hero stays put, otherwise camp as before), trail map (25; reveals every tile of this deck's valley, not counted as tiles mapped), compass (40; `#cp` in the HUD: arrow and steps to the nearest waiting creature, preferring ones that can be asked now; points at the hall chest when all are done), keepsakes (20; deck-written, each shows a fact).
- Deck texas-independence: 8 merchants, 15 keepsakes, every fact taken from that region's signpost notes.
- sw.py: `check` validates merchant goods; `records` lists purchases.
- Verified in Chrome on 127.0.0.1:18768 (clean origin, cleared after): flood-fill reaches 90 of 90 creatures and 8 of 8 merchants; with 10 gold only the potion can be bought; with 500 gold every good bought once (gold 500 to 395), keepsakes show "In your pack" with the fact, map "Already mapped", compass text shown; a miss at 1 heart with a potion keeps the hero in place with full hearts, without one wakes at camp; walking into the trader opens the shop; no console errors. All seven games rebuilt; verify_lesson.js passes.
- Small rulings: no hint or skip items (guard rail in learning-design.md: nothing skips a question or hides the explanation); merchants are opt-in per region so Breeders' Valley is unchanged; a Ranger's starting compass and every hero's starting potion now work in world mode; facts are escaped plain text; the bell is not mentioned in the Bell of Dolores fact because the guide does not mention it.
- Fixed on the way: the HUD kept showing 0 hearts after waking at camp.
- Not done: wiki update; evergreen-refresh of the due units; the finish download was not run again (unchanged code).

## 2026-11-12 session 15 | study RPG split out to studyquest (0.11.0)
- Mark: split the son's RPG study game into its own repo to improve by itself; studywright is for the building, the techniques and a knowledge base of learning game development; the game should one day be a free Steam release, and lexwright should check for complications with a public or a private repo.
- Mark's answers (asked in chat): working name studyquest; studywright keeps the quiz and lesson builders.
- New private repo m4bwav/studyquest at D:/m4bwa/Claude/Projects/Ai/studyquest: engine/ (the three templates and kit.js), tools/sq.py (sw.py with the folder name changed), the seven decks, rebuilt games (byte-identical to the last studywright builds), docs/ and its own ai-docs. records/ was copied there (diff -rq identical) and removed here.
- Here: removed templates/world.html, the world checks, `order` and `fig` from sw.py (a world deck now fails `check` with a pointer), the seven decks, games/ and juice-changes.md; added decks/sample-states-of-matter.json (12 questions, written from scratch) and decks/sample-mean-absolute-deviation.json (the lesson deck without banned_hashes). Both samples build; verify_lesson.js and verify_routes.py pass on the lesson sample.
- Small rulings: the split is a copy with fresh history, so the old decks stay in this public repo's history; lesson mode exists in both repos for now; installed heroes and the shared land are in browser storage and are not touched.
- Not done: the lexwright check (its notice needs Mark's typed "I agree" first); wiki update; lesson mode variation.

## 2026-11-13 - 0.12.0 book harvest
- Adopted book-harvest items (Kapp, Chou, Werbach, Edutopia, Field Day Lab, Klopfer notes in technique-harvest) built in: learning-design.md gains content-to-form table, MC checklist, pre-brief/debrief, delayed retest, named failures, co-play and lesson-note ideas. sw.py check WARNs on length clues and all/none of the above. game.html: `practice` deck key, skill word beside score, debrief question.
