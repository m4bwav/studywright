import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import sw


def run(d):
    sw.WARNS.clear()
    sw.check_praise(d)
    return list(sw.WARNS)


def test_deck_reward_names_warn():
    w = run({"questions": [], "feats": [{"name": "Born Genius"}], "badges": ["Epic Fail"],
             "titles": {"slow": "Slowpoke"}})
    assert len(w) == 3, w


def test_deck_reward_names_quiet():
    assert run({"questions": [], "feats": [{"name": "Grit"}, {"name": "Second Wind"}],
                "badges": ["Almost There", "Checked the Units"], "titles": ["Naturalist"]}) == []


def test_engine_names():
    bad = "const FEATS={x:{name:'Butterfingers',desc:'...'}};opts.push({label:'Feat: Clever Clogs'});badge:\"Loser\""
    assert [h[1] for h in sw.lint_names(bad)] == ["Butterfingers", "Feat: Clever Clogs", "Loser"]
    ok = "const FEATS={keen:{name:'Keen Eye'},grit:{name:'Grit'}};title:'Failsafe Builder';name:'Second Wind'"
    assert sw.lint_names(ok) == []


def test_templates_clean():
    root = Path(__file__).resolve().parent.parent / "templates"
    for f in list(root.glob("*.html")) + [root / "kit.js"]:
        assert sw.lint_names(f.read_text(encoding="utf-8")) == [], f.name


if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
    print("ok")
