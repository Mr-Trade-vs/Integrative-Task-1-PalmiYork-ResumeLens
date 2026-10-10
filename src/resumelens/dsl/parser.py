from pathlib import Path
try:
    from textx import metamodel_from_file
except ImportError:
    metamodel_from_file = None

GRAMMAR_PATH = Path(__file__).with_name("candidate_profile.tx")

def build_metamodel():
    if metamodel_from_file is None:
        raise RuntimeError("textX is required. Install dependencies with: pip install -r requirements.txt")
    return metamodel_from_file(str(GRAMMAR_PATH))

def validate(text: str):
    mm = build_metamodel()
    return mm.model_from_str(text)
