import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import sw

def run(d):
    sw.WARNS.clear()
    return sw.check_reuse(d), list(sw.WARNS)

def mc(**k):
    return {"q": "x", "choices": ["a", "b"], "answer": 0, **k}

def test_misconception_once_warns():
    e, w = run({"questions": [mc(mis="choose-to-change"), mc()]})
    assert e == [] and len(w) == 1 and "MISCONCEPTION-ONCE" in w[0]

def test_misconception_three_items_quiet():
    qs = [mc(mis="m"), mc(mis=["m"]), mc(variants=[mc(mis="m")])]
    assert run({"questions": qs}) == ([], [])

def test_pair_on_one_item_fails():
    e, _ = run({"questions": [mc(pair="p1"), mc()]})
    assert len(e) == 1 and "pair" in e[0]

def test_big_math_deck_without_pair_warns():
    _, w = run({"subject": "Math: ratios", "questions": [mc(topic=str(i)) for i in range(20)]})
    assert any("'pair'" in x for x in w)
    _, w = run({"subject": "Math: ratios", "questions": [mc(topic=str(i), pair=i // 2) for i in range(20)]})
    assert w == []

def test_key_no_why_warns_and_quiet():
    _, w = run({"questions": [mc(topic="T")] * 5})
    assert len(w) == 1 and "KEY-NO-WHY" in w[0]
    qs = [mc(topic="T")] * 4 + [mc(topic="T", why={"choices": ["real", "myth"], "answer": 0})]
    assert run({"questions": qs}) == ([], [])

def test_bad_why_fails():
    e, _ = run({"questions": [mc(why={"choices": ["a"], "answer": 3}), mc(why="no")]})
    assert len(e) == 3

def test_science_needs_predict():
    qs = [mc(topic=str(i)) for i in range(15)]
    _, w = run({"subject": "Science: forces", "questions": qs})
    assert any("predict" in x for x in w)
    qs[0] = mc(topic="0", q="What will happen if you push the cart harder?")
    _, w = run({"subject": "Science: forces", "questions": qs})
    assert not any("predict" in x for x in w)

if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
    print("ok")
