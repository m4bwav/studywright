import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from sw import check_objectives

def test_no_objectives_is_fine():
    assert check_objectives({"questions": [{"q": "a"}]}) == []

def test_every_objective_covered():
    d = {"objectives": ["melt", "boil"], "questions": [{"objective": "melt"}, {"objective": "boil"}, {}]}
    assert check_objectives(d) == []

def test_uncovered_objective_fails():
    d = {"objectives": ["melt", "boil"], "questions": [{"objective": "melt"}]}
    assert check_objectives(d) == ["objective 'boil' has no question that tests it"]

def test_unknown_objective_fails():
    d = {"objectives": ["melt"], "questions": [{"objective": "melt"}, {"objective": "freeze"}]}
    assert check_objectives(d) == ["q2: objective 'freeze' is not in the deck's 'objectives' list"]

def test_bad_shape_fails():
    assert check_objectives({"objectives": "melt"})

if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
    print("ok")
