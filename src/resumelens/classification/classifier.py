from resumelens.core.models import ClassificationResult
from .automata import accepts, explain

def classify(sorted_by_profile: dict[str, list[str]], profiles: dict) -> list[ClassificationResult]:
    results = []
    for name, profile in profiles.items():
        seq = sorted_by_profile[name]
        required = profile["required"]
        accepted = accepts(seq, required)
        results.append(ClassificationResult(name, accepted, seq, explain(seq, required)))
    return results
