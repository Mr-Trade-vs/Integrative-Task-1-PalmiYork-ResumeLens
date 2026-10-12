try:
    from pyformlang.fst import FST
except ImportError:
    FST = None

NORMALIZATION = {
    "js": "JAVASCRIPT", "javascript": "JAVASCRIPT", "typescript": "TYPESCRIPT", "ts": "TYPESCRIPT",
    "react.js": "REACT", "reactjs": "REACT", "react": "REACT",
    "nodejs": "NODE_JS", "node.js": "NODE_JS", "node": "NODE_JS",
    "postgres": "POSTGRESQL", "postgresql": "POSTGRESQL",
    "pandas": "PANDAS", "sklearn": "SCIKIT_LEARN", "scikit-learn": "SCIKIT_LEARN", "scikit learn": "SCIKIT_LEARN",
    "tensorflow": "TENSORFLOW", "tensor flow": "TENSORFLOW",
    "pytorch": "PYTORCH", "py torch": "PYTORCH",
    "python": "PYTHON", "fastapi": "FASTAPI", "rest": "REST_API", "restful": "REST_API", "rest api": "REST_API",
    "docker": "DOCKER", "git": "GIT", "numpy": "NUMPY", "sql": "SQL",
    "mysql": "MYSQL", "mongodb": "MONGODB", "mongo": "MONGODB"
}

def build_pyformlang_transducer():
    """Build the alias-to-canonical-symbol transducer when pyformlang is available."""
    if FST is None:
        return None
    fst = FST()
    for raw, canonical in NORMALIZATION.items():
        fst.add_transition("q0", raw, "qf", [canonical])
    fst.add_start_state("q0")
    fst.add_final_state("qf")
    return fst

_TRANSDUCER = build_pyformlang_transducer()


def normalize_one(value: str) -> str | None:
    alias = value.strip().lower()
    if _TRANSDUCER is None:
        # Keep the app usable in environments that have not installed requirements.txt.
        return NORMALIZATION.get(alias)

    translations = list(_TRANSDUCER.translate([alias]))
    if not translations or not translations[0]:
        return None
    return translations[0][0]

def normalize(values: list[str]) -> tuple[list[str], dict[str, str]]:
    mapping = {}
    normalized = []
    for value in values:
        canonical = normalize_one(value)
        if canonical:
            mapping[value] = canonical
            if canonical not in normalized:
                normalized.append(canonical)
    return normalized, mapping
