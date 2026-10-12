from resumelens.classification.automata import accepts, explain

def test_full_stack_pattern_accepts_required_sequence():
    order = ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"]
    assert accepts(order, order)

def test_extra_qualification_is_allowed():
    order = ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"]
    assert accepts([*order, "DOCKER"], order)

def test_missing_qualification_is_rejected():
    order = ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"]
    assert not accepts(["JAVASCRIPT", "REACT", "NODE_JS", "GIT"], order)
    assert "missing" in explain(["JAVASCRIPT"], order)
