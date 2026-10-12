from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State, Symbol
from resumelens.normalization.transducer import NORMALIZATION


CANONICAL_ALPHABET = set(NORMALIZATION.values())


def build_dfa(order: list[str]) -> DeterministicFiniteAutomaton:
    """Build a DFA that accepts the required symbols in order, ignoring extras."""
    dfa = DeterministicFiniteAutomaton()
    states = [State(f"q{i}") for i in range(len(order) + 1)]

    # Normalization discards unknown terms, so every remaining qualification
    # must have a transition in the profile DFA, including non-required ones.
    alphabet = CANONICAL_ALPHABET | set(order)
    for i, token in enumerate(order):
        for other in alphabet:
            target = states[i + 1] if other == token else states[i]
            dfa.add_transition(states[i], Symbol(other), target)

    for other in alphabet:
        dfa.add_transition(states[-1], Symbol(other), states[-1])

    dfa.add_start_state(states[0])
    dfa.add_final_state(states[-1])
    return dfa


def accepts(sequence: list[str], order: list[str]) -> bool:
    dfa = build_dfa(order)
    return dfa.accepts([Symbol(token) for token in sequence])


def explain(sequence: list[str], required: list[str], accepted: bool | None = None) -> str:
    missing = [x for x in required if x not in sequence]
    if accepted is None:
        accepted = accepts(sequence, required)
    if accepted:
        return "ACCEPTED: the canonical sequence reaches the accepting state; extra qualifications are treated as self-loops."
    if missing:
        return "REJECTED: missing required qualifications: " + ", ".join(missing) + "."
    return "REJECTED: qualifications were found but the canonical profile pattern was not satisfied."
