from pyformlang.fst import FST

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

def build_pyformlang_FST():
    fst = FST()

    for raw, canonical in NORMALIZATION.items():
        fst.add_transition(
            "q0",
            raw,
            "qf",
            [canonical]
        )

    fst.add_start_state("q0")
    fst.add_final_state("qf")

    return fst

_NORMALIZATION_FST = build_pyformlang_FST()


def normalize_one(value: str) -> str | None:
    raw = value.strip().lower()

    if not raw:
        return None

    outputs = list(_NORMALIZATION_FST.translate([raw]))

    if not outputs or not outputs[0]:
        return None

    return outputs[0][0]


def normalize(values: list[str]) -> tuple[list[str], dict[str, str]]:
    mapping = {}
    normalized = []

    for value in values:
        canonical = normalize_one(value)

        if canonical is not None:
            mapping[value] = canonical

            if canonical not in normalized:
                normalized.append(canonical)

    return normalized, mapping
