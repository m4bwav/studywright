import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import sw

def run(d):
    sw.WARNS.clear()
    return sw.check_hooks(d), list(sw.WARNS)

def test_bare_fact_deck_warns():
    e, w = run({"questions": [{"type": "type"}] * 5})
    assert e == [] and len(w) == 1 and "hook" in w[0]

def test_one_hook_is_quiet():
    e, w = run({"questions": [{"type": "type"}] * 4 + [{"type": "type", "hook": "Baker the baker"}]})
    assert e == [] and w == []

def test_few_typed_items_quiet():
    assert run({"questions": [{"type": "type"}] * 4 + [{"type": "mc"}] * 10}) == ([], [])

def test_bad_hook_fails():
    e, _ = run({"questions": [{"hook": ""}, {"hook": 3}]})
    assert len(e) == 2

if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
    print("ok")
