# Stage 1 — Regular Expressions

## Contact email

**Pattern:** `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`

Recognizes conventional email addresses containing a local part, `@`, domain and alphabetic top-level domain.

## Experience

**Pattern:** `\b(\d+)\+?\s+years?\s+(of\s+)?(professional\s+)?experience\b`

Recognizes an integer followed by `year`/`years` and the word `experience`, allowing optional `+`, `of`, and `professional`.

## Qualifications

The project uses finite vocabularies for programming languages, frameworks/libraries, databases and tools. The patterns are case-insensitive and accept common spelling variants needed by the project.

The implementation is in `src/resumelens/extraction/regex_extractor.py`.
