# studywright

![A worksheet on a study desk with glowing quiz cards, gems and a small block tower rising from it](https://raw.githubusercontent.com/m4bwav/studywright/main/.github/images/banner.jpg)

Photos of a worksheet in, a study game out. Each game is one HTML file that runs offline in any browser:

- asks about every blank and every row of the sheet, multiple choice and typed answers (typos forgiven);
- says right or wrong after each answer and **why**;
- puts a missed question back a few turns later until it is answered right (mastery, not one pass);
- XP, levels, streak bonus (gold blocks, double XP at 3+), a 3D tower that grows with every right answer, sounds, and a "review these before the test" list with answers at the end.

```
python skills/studywright/scripts/sw.py build skills/studywright/decks/sample-states-of-matter.json games/sample-states-of-matter.html
```

Deck format and the learning design rules are in [skills/studywright/SKILL.md](skills/studywright/SKILL.md). A second builder, lesson mode, teaches a method step by step before it tests it.

The plugin is also a knowledge base on building learning games: the research is in [RESEARCH.md](skills/studywright/RESEARCH.md) and the design rules, with what each build taught, are in [learning-design.md](skills/studywright/references/learning-design.md). The open-world study RPG that started here is now a separate game.

## Works with

- **[ludowright](https://github.com/m4bwav/ludowright)**: designing a commercial game belongs to ludowright; studywright builds learning games and decks.
- **[everscout](https://github.com/m4bwav/everscout)**: the `learning-games` beat feeds new research and tools into studywright's refreshes.
- **[askwright](https://github.com/m4bwav/askwright)**: choices about a learner's deck or schedule that need a person (what to drop, how hard to push) can go on an askwright page.

The wiki's [Works with](https://github.com/m4bwav/studywright/wiki/Works-with) page describes each pairing in more detail.
