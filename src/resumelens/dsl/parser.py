from pathlib import Path
try:
    from textx import metamodel_from_file
    from textx.exceptions import TextXError
except ImportError:
    metamodel_from_file = None
    TextXError = Exception

GRAMMAR_PATH = Path(__file__).with_name("candidate_profile.tx")


class CandidateProfileValidationError(ValueError):
    """Raised when generated candidate-profile text violates the DSL grammar."""


def build_metamodel():
    if metamodel_from_file is None:
        raise RuntimeError("textX is required. Install dependencies with: pip install -r requirements.txt")
    return metamodel_from_file(str(GRAMMAR_PATH))

def validate(text: str):
    mm = build_metamodel()
    try:
        return mm.model_from_str(text)
    except TextXError as exc:
        raise CandidateProfileValidationError(
            f"Generated candidate profile does not match the DSL grammar: {exc}"
        ) from exc
