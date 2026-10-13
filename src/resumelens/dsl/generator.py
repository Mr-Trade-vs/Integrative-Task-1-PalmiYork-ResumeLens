def q(value: str | None) -> str:
    """Escape quotes using textX's STRING rule and preserve literal backslashes."""
    value = value or ""
    return '"' + value.replace('"', '\\"') + '"'


def generate(candidate, classifications, normalized_qualifications: list[str]) -> str:
    lines = [f"candidate {q(candidate.name)} {{"]
    lines.append(f"  contact {{ {q(candidate.email)} {q(candidate.phone)} }}")
    if candidate.years_experience is not None:
        lines.append(
            f"  experience {q('Resume')} {q('Professional Experience')} "
            f"{candidate.years_experience};"
        )
    for edu in candidate.education:
        lines.append(f"  education {q(edu)};")
    for skill in normalized_qualifications:
        lines.append(f"  skill {q(skill)};")
    for result in classifications:
        status = "ACCEPTED" if result.accepted else "REJECTED"
        lines.append(
            f"  classification {result.profile.replace(' ', '_')} {status} "
            f"{q(result.explanation)};"
        )
    lines.append("}")
    return "\n".join(lines)
