import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from verify_xp import scan, easy_pays_more, game_choices, xp_per_min

def test_ok():
    assert scan("h.xp+=gain;S.xp+=gain;const h={xp:0};const xp=a*20;h.inv.gold+=S.gold;g=rnd(2,4)+(gold?2:0)") == []

def test_breaks():
    for bad in ["h.xp-=5", "h.xp=10", "h.xp--", "I.gold+=h.xp", "h.xp+=I.gold", "{xp:-3}"]:
        assert scan(bad), bad

def test_easy_pays_more_warns():
    cs = [{"group": "deck", "name": "easy", "level": 1, "xp": 10, "secs": 6, "acc": 1.0},
          {"group": "deck", "name": "hard", "level": 2, "xp": 10, "secs": 20, "acc": 0.7}]
    w = easy_pays_more(cs)
    assert len(w) == 1 and "easier 'easy'" in w[0]

def test_fair_table_quiet():
    cs = [{"group": "deck", "name": "easy", "level": 1, "xp": 5, "secs": 10, "acc": 0.95},
          {"group": "deck", "name": "hard", "level": 2, "xp": 20, "secs": 20, "acc": 0.7},
          # other groups are never compared with this one
          {"group": "mode", "name": "fast", "level": 0, "xp": 99, "secs": 1}]
    assert easy_pays_more(cs) == []

def test_tolerance():
    cs = [{"group": "g", "name": "a", "level": 1, "xp": 10.5, "secs": 60},
          {"group": "g", "name": "b", "level": 2, "xp": 10, "secs": 60}]
    assert easy_pays_more(cs) == [] and len(easy_pays_more(cs, tol=0.0)) == 1
    assert xp_per_min(cs[1]) == 10

def test_game_table_reads_award_line():
    cs = game_choices("let gain=(gold?20:10)+area(h,STAT).lvl;")
    assert [c["level"] for c in cs] == [1, 2] and all(c["xp"] > 10 for c in cs)
    assert game_choices("no award here") == []

if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
    print("ok")
