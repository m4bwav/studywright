import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import sw

def run(d):
    sw.WARNS.clear()
    sw.check_praise(d)
    return list(sw.WARNS)

def test_trait_praise_warns():
    w = run({"intro": "Show how smart you are!", "questions": [{"win": "{h}, you genius!"}]})
    assert len(w) == 2

def test_effort_praise_quiet():
    assert run({"intro": "Practice pays off.", "questions": [{"win": "You fixed it on the second try.", "explain": "Natural selection acts on traits."}]}) == []

if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
    print("ok")
