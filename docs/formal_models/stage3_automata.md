# Stage 3 — Qualification Pattern Automata

## General 5-tuple

Each profile is modeled as a DFA:

**M = (Q, Σ, δ, q0, F)**

For an order of `n` required qualifications:

- **Q** = `{q0, q1, ..., qn}`
- **Σ** = canonical qualification symbols used by the profile
- **δ** = expected qualification advances the state; other symbols self-loop
- **q0** = initial state
- **F** = `{qn}`

The canonical sorting stage places required qualifications in the profile's expected order. This makes the DFA interpretation explicit and deterministic.

## Full Stack Developer

Pattern:

`JAVASCRIPT → REACT → NODE_JS → POSTGRESQL → GIT`

## Machine Learning Engineer

Pattern:

`PYTHON → PANDAS → SCIKIT_LEARN → TENSORFLOW → POSTGRESQL → GIT`

## Backend Developer

Pattern:

`PYTHON → FASTAPI → POSTGRESQL → REST_API → DOCKER → GIT`

## Data Scientist

Pattern:

`PYTHON → PANDAS → NUMPY → SCIKIT_LEARN → SQL → GIT`

## Generic diagram

```text
(q0) --required1--> (q1) --required2--> ... --requiredN--> ((qN))
  |                    |                                  |
  +--other symbols----+--other symbols-------------------+  self-loop
```

The implementation uses `pyformlang.finite_automaton.DeterministicFiniteAutomaton` when installed.
