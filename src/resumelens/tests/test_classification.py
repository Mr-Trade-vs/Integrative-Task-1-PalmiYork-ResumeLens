from pyformlang.finite_automaton import DeterministicFiniteAutomaton, Symbol

from resumelens.classification.automata import accepts, build_dfa, explain

def test_full_stack_pattern_accepts_required_sequence():
    order = ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"]
    assert accepts(order, order)

def test_extra_qualification_is_allowed():
    order = ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"]
    assert accepts([*order, "DOCKER"], order)


def test_build_dfa_uses_pyformlang_and_allows_extra_canonical_symbols():
    order = ["JAVASCRIPT", "REACT", "NODE_JS"]
    dfa = build_dfa(order)

    assert isinstance(dfa, DeterministicFiniteAutomaton)
    assert dfa.accepts([Symbol("JAVASCRIPT"), Symbol("PYTHON"), Symbol("REACT"), Symbol("NODE_JS")])


def test_missing_qualification_is_rejected():
    order = ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"]
    assert not accepts(["JAVASCRIPT", "REACT", "NODE_JS", "GIT"], order)
    assert "missing" in explain(["JAVASCRIPT"], order)


def test_required_order_is_enforced_by_the_dfa():
    order = ["JAVASCRIPT", "REACT", "NODE_JS"]

    assert not accepts(["REACT", "JAVASCRIPT", "NODE_JS"], order)


def test_classification_result_exposes_required_and_missing_qualifications():
    from resumelens.classification.classifier import classify

    results = classify(
        {"Backend Developer": ["PYTHON", "FASTAPI", "POSTGRESQL"]},
        {"Backend Developer": {"required": ["PYTHON", "FASTAPI", "POSTGRESQL", "REST_API"]}},
    )

    assert results[0].required == ["PYTHON", "FASTAPI", "POSTGRESQL", "REST_API"]
    assert results[0].missing == ["REST_API"]
