# Lesson mode, a path map, and tonight's mean absolute deviation game

Work in `D:/m4bwa/Claude/Projects/Ai/studywright`. Read AGENTS.md, ai-docs/HANDOFF.md, the last three entries of ai-docs/log.md, skills/studywright/SKILL.md and skills/studywright/references/learning-design.md before anything else.

## The situation

Mark's son has a math worksheet due tomorrow (Friday 2026-11-13) on mean absolute deviation. He is strong at math, but this method is new to him and he cannot start the first questions. Mark wants him to play a studywright game tonight that teaches him how to do it, and then do the worksheet himself. It is already late and there is more homework after this one, so two things follow:

- The game takes ten minutes at most, start to finish, for a child who has never worked out a mean absolute deviation, counting the reading and the arithmetic on paper.
- Mark is waiting for the link. Hand it over as soon as the game teaches correctly and plays through, in a message of its own, and keep working after that. Polish, release work and docs all come after the link, never before it.

The worksheet, its number profile and an answer key are in `records/mean-absolute-deviation/worksheet.md`, with the photo beside it. That folder is gitignored and stays that way. The game prepares him for the worksheet; it must not do the worksheet. None of the worksheet's data sets, settings or question wording may appear in the deck or the game, and no question in the game may be one of its questions with the names changed. Invent other settings and other numbers of the same kind: five whole-number values with a whole-number mean, so the answer has at most one decimal place.

## What he has to be able to do afterwards

1. Find the mean of a small data set, and say by eye which of two sets has the higher mean and why.
2. Say by eye which of two sets is more spread out and why.
3. Work out a mean absolute deviation: find the mean, find each value's distance from the mean (never negative, and 0 when the value equals the mean), add the distances, divide by the number of values.
4. Read a mean absolute deviation: a larger one means more variability and less consistency. It says nothing about how large the values are.
5. Combine the two measures: a set can have a high or low mean and, separately, a high or low mean absolute deviation, and a comparison of variability needs the figure for both sets. "Consistent and high" means a high mean with a low mean absolute deviation.

## Why this needs a new mode

Every studywright game so far is retrieval practice: it asks first and explains after, because the student has already met the material. Here he has not, so asking first would only make him guess. The new mode teaches, then hands over: show one worked example, then one with the last steps left for him, then a whole problem by himself. He is quick, so keep the shown part short and let him move to solo work as soon as he gets it right; one clean pass through each idea is enough, and arithmetic drills would waste his ten minutes.

What the mode needs that the engine lacks today (the engine is `skills/studywright/templates/game.html`, 351 dense lines):

- **Number answers**, compared as numbers, so 7.6, 7.60 and " 7.6" all count, with a number keyboard on touch screens.
- **Fresh numbers each time.** A procedure question should draw its data set from a generator, so a second try cannot be answered from memory and the game is worth replaying. The four existing decks hold fixed text only.
- **Feedback that names the slip.** For a wrong mean absolute deviation, compute the likely wrong answers for that data set and say which one he gave: the mean itself, the sum of the distances not yet divided, 0 from keeping the minus signs, a wrong divisor. Then show the worked steps for that same set. Use the same slips as the wrong choices in multiple-choice items.
- **A picture of distance.** A number line or dot plot with the mean marked and a bar from each value to the mean makes "distance from the mean" visible, and two of them side by side carry the predict-by-eye questions.
- **A fixed length.** The existing engine brings misses back until mastered, opens a boss round on misses, stops for level-up picks and a hero builder, and locks Next for three seconds after each answer. Any of these can push a run past ten minutes. In this mode a miss gets the worked steps and at most one retry with new numbers, then the run moves on and the skill goes on the end screen list. He starts with his existing hero in one click, and level-up picks wait for the end. Work out the node count from a time budget (a full five-value problem by hand takes him about two minutes) and write the budget in the log. Record the real elapsed time and the first-try result per skill in the record JSON so the next session can see how it went.

Make it a deck-level mode that any future how-to worksheet can use, not a one-off page. The four existing decks must build and play exactly as before.

## The path map

Mark wants a roguelike idea added: after each encounter the player chooses which way to go next, shown on a map. Build it for this mode. Give it its own look and node names; use the genre's branching map, not a copy of any one game's.

Two rules hold whatever the design: every route teaches all five skills, and every route has the same length. A choice may change the form of the next encounter, how hard it is and what it pays, but never whether a skill gets taught or how long the run lasts. One idea worth testing: let the choice be how much help he takes, a guided node (worked steps shown, small reward) against a solo node (harder set, larger reward). That makes the choice real and suits a strong student. Judge it with ludowright before settling.

## Order of work

1. Lesson mode, the generator, the map and the deck (`decks/mean-absolute-deviation.json`), then `sw.py check` and `build`. If the map turns out to be the slow part, hand over a lesson-only build first and add the map straight after.
2. Verify, then hand over the first link.
3. A ludowright round: invoke the `ludowright:ludowright` skill on the mode. Is the path choice a real, informed choice? Does anything reward guessing or rushing? Does the ten-minute pacing hold?
4. A juice round: invoke `game-juice:juice-scan`, then `game-juice:juice-apply` for the findings that fit: answer feedback, moving along the map, the distance bars, the last node. Juice must not add time to the run or block input, and it follows that skill's rules on toggles and reduced motion.
5. Rebuild, verify again, hand over the second link. Write what was left out of both rounds into HANDOFF.

## Verifying

A wrong answer key in a teaching game is the worst thing this session could ship, so check the math independently of the page code:

- A script that runs the generator a few thousand times and confirms every set fits the number profile, every expected answer matches a separate computation, and no worksheet data set can come out.
- A script that lists every route through the map and confirms each one covers all five skills in the same number of nodes.
- A browser play-test on 127.0.0.1 (port 18765; 8765 is refused on this machine): one clean run, one run that makes each named slip and sees its own feedback, number entry in its odd forms, the end screen, the downloaded record. Remove test heroes and restore localStorage afterwards, as earlier sessions did.
- All four older games rebuilt and opened once.

## Handing over

Give the game as a copyable browser link in a code span (`file:///D:/m4bwa/Claude/Projects/Ai/studywright/games/<slug>.html`), as SKILL.md step 6 says. Add three lines for Mark: what his son will have practised, that he needs paper and a pencil, and what the end screen tells Mark about readiness for the worksheet.

Decide small design questions yourself and list them in the reply. Nothing tonight should wait on Mark; anything that truly needs him goes on an askwright page while the work continues.

After the second link: update SKILL.md (when to choose lesson mode over quiz mode, the new deck keys), `sw.py check` for those keys, learning-design.md (why teach-then-fade, with sources in RESEARCH.md), CHANGELOG and the plugin version. Keep the child's name out of every file. Branch, pull request, merge, tag and release follow the standing rules in Mark's global instructions, then update the installed plugin.

Last, run the evergreen-wrapup skill, update ai-docs/HANDOFF.md and ai-docs/log.md, and print the standing start command:

`Execute D:/m4bwa/Claude/Projects/Ai/studywright/ai-docs/plans/2026-11-10-studywright-continue-prompt.md`
