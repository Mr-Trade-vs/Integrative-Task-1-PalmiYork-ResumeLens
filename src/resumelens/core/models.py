from dataclasses import dataclass, field
from typing import Any

@dataclass
class Candidate:
    name: str = "Unknown"
    email: str | None = None
    phone: str | None = None
    years_experience: int | None = None
    education: list[str] = field(default_factory=list)
    experiences: list[str] = field(default_factory=list)
    qualifications: list[str] = field(default_factory=list)

@dataclass
class ExtractionResult:
    candidate: Candidate
    raw_matches: dict[str, list[str]]

@dataclass
class NormalizationResult:
    normalized: list[str]
    mapping: dict[str, str]
    sorted_by_profile: dict[str, list[str]]

@dataclass
class ClassificationResult:
    profile: str
    accepted: bool
    sequence: list[str]
    explanation: str
    required: list[str] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)

@dataclass
class PipelineResult:
    extraction: ExtractionResult
    normalization: NormalizationResult
    classifications: list[ClassificationResult]
    dsl_text: str
    html: str
