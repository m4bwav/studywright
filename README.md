# studywright

Photos of a worksheet in, a study game out. Each game is one HTML file that runs offline in any browser:

- asks about every blank and every row of the sheet, multiple choice and typed answers (typos forgiven);
- says right or wrong after each answer and **why**;
- puts a missed question back a few turns later until it is answered right (mastery, not one pass);
- XP, levels, streak bonus (gold blocks, double XP at 3+), a 3D tower that grows with every right answer, sounds, and a "review these before the test" list with answers at the end.

```
python skills/studywright/scripts/sw.py build skills/studywright/decks/natural-selection.json games/natural-selection.html
```

Deck format and the learning design rules are in [skills/studywright/SKILL.md](skills/studywright/SKILL.md).
