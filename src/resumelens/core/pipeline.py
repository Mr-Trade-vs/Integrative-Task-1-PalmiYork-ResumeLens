import argparse
from pathlib import Path
from resumelens.core.config import load_profiles
from resumelens.core.models import NormalizationResult, PipelineResult
from resumelens.extraction import extract
from resumelens.normalization.transducer import normalize
from resumelens.normalization.sorter import sort_for_profile
from resumelens.classification import classify
from resumelens.dsl.generator import generate
from resumelens.visualization import render

def process(text: str, profiles: dict | None = None) -> PipelineResult:
    profiles = profiles or load_profiles()
    extraction = extract(text)
    raw_values = extraction.candidate.qualifications
    normalized, mapping = normalize(raw_values)
    sorted_by_profile = {name: sort_for_profile(normalized, p["order"]) for name, p in profiles.items()}
    normalization = NormalizationResult(normalized, mapping, sorted_by_profile)
    classifications = classify(sorted_by_profile, profiles)
    dsl_text = generate(extraction.candidate, classifications)
    provisional = PipelineResult(extraction, normalization, classifications, dsl_text, "")
    provisional.html = render(provisional)
    return provisional

def main():
    parser = argparse.ArgumentParser(description="ResumeLens formal-language pipeline")
    parser.add_argument("resume", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("data/outputs"))
    args = parser.parse_args()
    result = process(args.resume.read_text(encoding="utf-8"))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = args.resume.stem
    (args.output_dir / f"{stem}.dsl").write_text(result.dsl_text, encoding="utf-8")
    (args.output_dir / f"{stem}.html").write_text(result.html, encoding="utf-8")
    for r in result.classifications:
        print(f"{r.profile}: {'ACCEPTED' if r.accepted else 'REJECTED'} — {r.explanation}")

if __name__ == "__main__":
    main()
