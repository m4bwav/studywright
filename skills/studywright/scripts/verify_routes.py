"""List every route through a lesson deck's map; each must teach every skill in the same number of stages."""
import itertools, json, sys
deck = json.load(open(sys.argv[1], encoding="utf-8"))
stages = deck["map"]
routes = list(itertools.product(["guided", "solo"], repeat=len(stages)))
lens, bad = set(), 0
for r in routes:
    taught = {s["skill"] for s in stages}  # both nodes of a stage run the same kind and skill
    lens.add(len(r))
    if taught != set(deck["skills"]):
        bad += 1
print(f"{len(routes)} routes, lengths {sorted(lens)}, {bad} missing a skill")
sys.exit(1 if bad or len(lens) != 1 else 0)
