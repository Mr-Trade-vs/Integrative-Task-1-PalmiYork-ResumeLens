try:
    from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State, Symbol
except ImportError:
    DeterministicFiniteAutomaton = State = Symbol = None

def build_dfa(order: list[str]):
    if DeterministicFiniteAutomaton is None:
        return None
    dfa = DeterministicFiniteAutomaton()
    states = [State(f"q{i}") for i in range(len(order) + 1)]
    alphabet = set(order)
    for i, token in enumerate(order):
        dfa.add_transition(states[i], Symbol(token), states[i + 1])
        for other in alphabet - {token}:
            dfa.add_transition(states[i], Symbol(other), states[i])
    for other in alphabet:
        dfa.add_transition(states[-1], Symbol(other), states[-1])
    dfa.add_start_state(states[0])
    dfa.add_final_state(states[-1])
    return dfa

def accepts(sequence: list[str], order: list[str]) -> bool:
    position = 0
    for token in sequence:
        if position < len(order) and token == order[position]:
            position += 1
    return position == len(order)

def explain(sequence: list[str], required: list[str]) -> str:
    missing = [x for x in required if x not in sequence]
    if not missing and accepts(sequence, required):
        return "ACCEPTED: the canonical sequence reaches the accepting state; extra qualifications are treated as self-loops."
    if missing:
        return "REJECTED: missing required qualifications: " + ", ".join(missing) + "."
    return "REJECTED: qualifications were found but the canonical profile pattern was not satisfied."
