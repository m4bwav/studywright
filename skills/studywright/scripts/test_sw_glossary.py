import json, shutil, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import sw

G = [
    {"term": "natural selection", "def": "The process whereby organisms better adapted to their environment tend to survive.", "plain": "Living things that fit their home better live longer and have more babies."},
    {"term": "selection", "def": "The act of choosing.", "plain": "Picking."},
    {"term": "trait", "def": "A distinguishing quality or characteristic.", "plain": "Something about you, like eye colour.", "aliases": ["feature"]},
]
CASES = [
    ("Natural selection acts on traits.", ["natural selection", "trait"]),
    ("Artificial selection is a choice.", ["selection"]),
    ("Two features differ.", ["trait"]),
    ("The bus has glass.", []),
    ("natural, selection", ["selection"]),
]


def terms(text):
    return [t for _, _, t in sw.gloss_find(text, sw.gloss_index(G))]


def test_longest_phrase_wins():
    assert terms(CASES[0][0]) == ["natural selection", "trait"]


def test_plural_fallback_and_alias():
    assert terms("Traits vary.") == ["trait"]
    assert terms("Two features differ.") == ["trait"]
    assert terms("The bus has glass.") == []  # words ending in ss never lose an s


def test_phrase_does_not_cross_punctuation():
    assert terms("natural, selection") == ["selection"]


def test_spans_point_at_the_words():
    t = "Big trait here"
    s, e, _ = sw.gloss_find(t, sw.gloss_index(G))[0]
    assert t[s:e] == "trait"


def run(g):
    sw.WARNS.clear()
    errs = sw.check_glossary({"glossary": g})
    return errs, list(sw.WARNS)


def test_check_rules():
    assert run(G) == ([], [])
    errs, _ = run([{"term": "x", "def": "a thing"}])
    assert len(errs) == 1 and "plain" in errs[0]
    errs, _ = run([{"term": "x", "plain": "a thing"}])
    assert len(errs) == 1 and "def" in errs[0]
    _, w = run([{"term": "x", "def": "short", "plain": "a much longer text"}])
    assert len(w) == 1 and "longer" in w[0]
    _, w = run([G[2], {"term": "Trait", "def": "d d d", "plain": "p"}])
    assert len(w) == 1 and "duplicate" in w[0]
    assert run("nope")[0]


def test_js_twin_agrees():
    node = shutil.which("node")
    if not node:
        return
    js = (Path(__file__).parent.parent / "templates" / "glossary.js").read_text(encoding="utf-8")
    src = "const DECK=" + json.dumps({"glossary": G}) + ";\n" + js + "\nconsole.log(JSON.stringify(" + json.dumps([c for c, _ in CASES]) + ".map(t=>GL.find(t).map(h=>h.entry.term))))"
    got = json.loads(subprocess.run([node, "-e", src], capture_output=True, text=True, check=True).stdout)
    assert got == [want for _, want in CASES], got


if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
    print("ok")
