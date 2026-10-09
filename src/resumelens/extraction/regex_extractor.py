import re
from resumelens.core.models import Candidate, ExtractionResult

PATTERNS = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone": re.compile(r"(?<!\d)(?:\+?\d[\d\s().-]{7,}\d)(?!\d)"),
    "years_experience": re.compile(r"\b(\d+)\+?\s+years?\s+(?:of\s+)?(?:professional\s+)?experience\b", re.I),
    "programming_languages": re.compile(r"\b(?:JavaScript|Javascript|JS|TypeScript|TS|Python|Java|C#|C\+\+|Go|Golang|Ruby|PHP|Kotlin|Swift|SQL)\b", re.I),
    "frameworks_libraries": re.compile(r"\b(?:React(?:\.js|JS)?|Angular|Vue(?:\.js)?|Node(?:\.js|JS)?|Django|Spring\s*Boot|Express(?:\.js)?|FastAPI|Flask|Pandas|NumPy|Scikit[- ]learn|sklearn|TensorFlow|PyTorch|Keras)\b", re.I),
    "databases": re.compile(r"\b(?:PostgreSQL|Postgres|MySQL|MariaDB|MongoDB|Mongo|Redis|SQLite|Oracle|SQL Server|DynamoDB)\b", re.I),
    "tools": re.compile(r"\b(?:Git|Docker|Kubernetes|Jenkins|AWS|Azure|GCP|Linux|REST(?:ful)?|GraphQL|Kafka)\b", re.I),
    "education": re.compile(r"\b(?:BSc|MSc|Bachelor(?:'s)?|Master(?:'s)?|PhD|Doctorate|Computer Science|Software Engineering|Data Science|Statistics|Mathematics)\b", re.I),
}

def _unique(items: list[str]) -> list[str]:
    seen = set(); out = []
    for item in items:
        key = item.lower()
        if key not in seen:
            seen.add(key); out.append(item)
    return out

def extract(text: str) -> ExtractionResult:
    matches = {name: _unique(pattern.findall(text)) for name, pattern in PATTERNS.items()}
    years = matches["years_experience"]
    candidate = Candidate(
        name=(text.strip().splitlines()[0].strip() if text.strip() else "Unknown"),
        email=matches["email"][0] if matches["email"] else None,
        phone=matches["phone"][0] if matches["phone"] else None,
        years_experience=int(years[0]) if years else None,
        education=matches["education"],
        experiences=([f"{years[0]} years of experience"] if years else []),
        qualifications=_unique(matches["programming_languages"] + matches["frameworks_libraries"] + matches["databases"] + matches["tools"]),
    )
    return ExtractionResult(candidate=candidate, raw_matches=matches)
