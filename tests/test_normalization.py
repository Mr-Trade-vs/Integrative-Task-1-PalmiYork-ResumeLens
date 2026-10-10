from resumelens.normalization import normalize, sort_for_profile

def test_aliases_normalize_to_canonical_tokens():
    values, mapping = normalize(["JS", "React.js", "NodeJS", "Postgres", "Git"])
    assert values == ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"]
    assert mapping["JS"] == "JAVASCRIPT"

def test_sorting_is_profile_specific():
    values = ["GIT", "POSTGRESQL", "NODE_JS", "REACT", "JAVASCRIPT"]
    order = ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"]
    assert sort_for_profile(values, order) == order
