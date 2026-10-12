# Stage 2 — Finite-State Transducer Formalization

ResumeLens models qualification normalization as one finite-state transducer whose input symbols are supported aliases and whose output symbols are canonical qualifications.

## General 7-tuple

For each alias mapping transducer:

**M = (Q, Σ, Γ, δ, ω, q0, F)**

- **Q** = `{q0, qf}`
- **Σ** = finite input alphabet containing the alias strings used by the project
- **Γ** = finite output alphabet containing canonical qualification symbols
- **δ** = transition relation containing `(q0, alias, qf)` for every supported alias
- **ω** = output relation that emits the canonical token associated with each alias
- **q0** = initial state
- **F** = `{qf}`

Examples:

- `JS → JAVASCRIPT`
- `Javascript → JAVASCRIPT`
- `React.js → REACT`
- `ReactJS → REACT`
- `NodeJS → NODE_JS`
- `Postgres → POSTGRESQL`
- `sklearn → SCIKIT_LEARN`
- `scikit-learn → SCIKIT_LEARN`
- `Tensor Flow → TENSORFLOW`
- `PyTorch → PYTORCH`

These are project-defined transformations rather than the only possible aliases.

## Graphical representation

```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> qf: alias / canonical token
    qf --> [*]
```

The implementation constructs an `FST` from `pyformlang.fst`. Each transition consumes one complete extracted alias and emits one canonical qualification token. The normalizer calls the transducer's `translate` operation for each extracted qualification. The mapping table supplies the transducer's transitions and remains a fallback if pyformlang is unavailable, so the app can still run before the project dependencies are installed.
