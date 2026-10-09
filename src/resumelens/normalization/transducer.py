try:
    from pyformlang.finite_transducer import Transducer
except ImportError:
    Transducer = None

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
    if Transducer is None:
        return None
    fst = Transducer()
    for raw, canonical in NORMALIZATION.items():
        fst.add_transition("q0", raw, "qf", canonical)
    fst.add_start_state("q0")
    fst.add_final_state("qf")
    return fst

def normalize_one(value: str) -> str | None:
    return NORMALIZATION.get(value.strip().lower())

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
