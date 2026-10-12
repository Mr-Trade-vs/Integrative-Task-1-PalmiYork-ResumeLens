from resumelens.normalization.transducer import normalize
from resumelens.normalization.sorter import sort_for_profile
from resumelens.normalization.transducer import (
    FST,
    build_pyformlang_FST,
    normalize_one,
    normalize
)

print(normalize_one("JS"))
print(normalize_one("React.js"))
print(normalize_one("Postgres"))
print(normalize_one("Mongo"))
print(normalize_one("tecnologia_desconocida"))

print(normalize(["JS", "javascript", "React.js", "Git"]))

def test_aliases_normalize_to_canonical_tokens():
    values, mapping = normalize(["JS", "React.js", "NodeJS", "Postgres", "Git"])
    assert values == ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"]
    assert mapping["JS"] == "JAVASCRIPT"

def test_sorting_is_profile_specific():
    values = ["GIT", "POSTGRESQL", "NODE_JS", "REACT", "JAVASCRIPT"]
    order = ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"]
    assert sort_for_profile(values, order) == order

def test_fst_translates_alias_directly():
    fst = build_pyformlang_FST()
    outputs = list(fst.translate(["js"]))

    assert ["JAVASCRIPT"] in outputs