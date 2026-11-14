import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from verify_xp import scan

def test_ok():
    assert scan("h.xp+=gain;S.xp+=gain;const h={xp:0};const xp=a*20;h.inv.gold+=S.gold;g=rnd(2,4)+(gold?2:0)") == []

def test_breaks():
    for bad in ["h.xp-=5", "h.xp=10", "h.xp--", "I.gold+=h.xp", "h.xp+=I.gold", "{xp:-3}"]:
        assert scan(bad), bad

if __name__ == "__main__":
    test_ok(); test_breaks(); print("ok")
