# ResumeLens — Vocabulary Definition

## 1. Raw résumé alphabet

Let $U$ denote the alphabet of Unicode characters supported by the input representation.

A résumé is modeled as a finite string:

$$x ∈ U*$$

Here, $x$ represents the complete textual résumé. This definition describes the form of the input; it does not assert that the résumé is valid or that every word in it is a recognized qualification.

## 2. Regular-expression extraction

Regular expressions identify substrings that match defined textual patterns in the résumé.

For a regular expression $r$, let $L(r)$ denote the language of strings recognized by that expression.

The extraction component applies the patterns implemented with Python's `re` module to identify relevant information, including contact information, professional experience, academic information, programming languages, frameworks, databases, tools, and other qualifications required by the supported profiles.

Extraction doesn't determine whether two mentions are equivalent and doesn't classify the candidate.

## 3. Extracted mentions

An extracted mention is a substring found in the résumé by an extraction pattern.

Examples:

- JS
- JavaScript
- React.js
- NodeJS
- Postgres
- Scikit-learn

These strings retain their original textual representations until the normalization component processes them.

## 4. Canonical qualification vocabulary

Let $C$ denote the finite vocabulary of canonical qualification symbols supported by ResumeLens.

Examples:

- JAVASCRIPT
- REACT
- NODE_JS
- POSTGRESQL
- SCIKIT_LEARN

Each canonical symbol represents a qualification concept supported by the system. Multiple extracted mentions may map to the same canonical symbol.

## 5. Normalization

The normalization component maps supported textual variants to canonical qualification symbols.

For example, supported variants of JavaScript may map to JAVASCRIPT, and supported variants of PostgreSQL may map to POSTGRESQL.

Let $N$ denote the normalization operation over supported extracted mentions. A mention without a defined mapping must be handled according to an explicit policy; it must not be silently treated as a recognized qualification.

Normalization does not decide whether a candidate satisfies a professional profile.

## 6. Profile-specific alphabets

For each professional profile $p$, let $\Sigma p$ denote the set of canonical qualification symbols used by that profile's recognition model.

The profile-specific alphabet must be compatible with the output of normalization and the transitions defined by the corresponding automaton.

Shared symbols may belong to more than one profile-specific alphabet.

## 7. Candidate-profile language

The candidate-profile DSL uses a separate grammar to represent structured candidate information, including personal information, contact information, experience, education, skills, and profile-classification results.

The grammar validates the structure of a candidate-profile representation. It does not replace extraction, normalization, or profile recognition.

## 8. Scope and limitations

Accepting Unicode résumé text does not mean that every textual expression is recognized. ResumeLens supports defined patterns and a finite qualification vocabulary.