# Stage 4 — Candidate Profile Context-Free Language

## EBNF-style description

```ebnf
Model         ::= Candidate ;
Candidate     ::= "candidate" STRING "{" Contact {Experience} {Education} {Skill} {Classification} "}" ;
Contact       ::= "contact" "{" STRING STRING "}" ;
Experience    ::= "experience" STRING STRING INT ";" ;
Education     ::= "education" STRING ";" ;
Skill         ::= "skill" STRING ";" ;
Classification ::= "classification" ID RESULT [STRING] ";" ;
RESULT        ::= "ACCEPTED" | "REJECTED" ;
```

## Structural properties

- A candidate has one contact block.
- Experiences, education records and skills can repeat.
- Classification records can repeat for the four supported profiles.
- String literals preserve structured values without requiring a natural-language parser.
- `textX` constructs the object model and rejects representations that violate the grammar.

The executable grammar is `src/resumelens/dsl/candidate_profile.tx`.
