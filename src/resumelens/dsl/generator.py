def q(value: str | None) -> str:
    value = value or ""
    return '"' + value.replace('"', '\\"') + '"'

def generate(candidate, classifications) -> str:
    lines = [f"candidate {q(candidate.name)} {{"]
    lines.append(f"  contact {{ {q(candidate.email)} {q(candidate.phone)} }}")
    years = candidate.years_experience or 0
    lines.append(f"  experience {q('Resume')} {q('Professional Experience')} {years};")
    for edu in candidate.education:
        lines.append(f"  education {q(edu)};")
    for skill in candidate.qualifications:
        lines.append(f"  skill {q(skill)};")
    for result in classifications:
        status = "ACCEPTED" if result.accepted else "REJECTED"
        lines.append(f"  classification {result.profile.replace(' ', '_')} {status};")
    lines.append("}")
    return "\n".join(lines)
