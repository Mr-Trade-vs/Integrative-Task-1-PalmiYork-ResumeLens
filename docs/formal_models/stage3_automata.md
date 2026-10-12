# Stage 3 — Qualification Pattern Automata

## General 5-tuple

Each profile is modeled as a DFA:

**M = (Q, Σ, δ, q0, F)**

For an order of `n` required qualifications:

- **Q** = `{q0, q1, ..., qn}`
- **Σ** = canonical qualification symbols emitted by the normalization stage, together with any required profile symbols
- **δ** = the next required qualification advances the state; every other symbol in `Σ` self-loops
- **q0** = initial state
- **F** = `{qn}`

The classifier constructs this DFA with `pyformlang.finite_automaton.DeterministicFiniteAutomaton` and evaluates the canonical sequence with the automaton's `accepts` method. The canonical sorting stage places required qualifications in the profile's expected order, so a candidate's original résumé ordering does not affect the result. Recognized qualifications outside the profile's requirements use self-loops.

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

The profile criteria and their expected sequence remain configured in `config/profiles.json`; the same DFA construction and evaluation logic is used for all four profiles.
