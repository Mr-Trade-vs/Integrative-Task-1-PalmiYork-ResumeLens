from html import escape

def render(profile_model) -> str:
    """Render a candidate-profile model already parsed and validated by textX."""
    c = profile_model.candidate
    qualifications = "".join(f"<li>{escape(item.value)}</li>" for item in c.skill)
    education = "".join(f"<li>{escape(item.value)}</li>" for item in c.education)
    experience = "".join(
        f"<li>{item.years} years — {escape(item.role)} at {escape(item.company)}</li>"
        for item in c.experience
    )
    classifications = "".join(
        f"<tr><td>{escape(item.profile.replace('_', ' '))}</td>"
        f"<td class='{('ok' if item.result == 'ACCEPTED' else 'no')}'>{escape(item.result)}</td>"
        f"<td>{escape(item.explanation or '')}</td></tr>"
        for item in c.classification
    )
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>ResumeLens - {escape(c.name)}</title>
<style>body{{font-family:Arial,sans-serif;max-width:900px;margin:40px auto;padding:0 20px}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #ddd;padding:8px;text-align:left}}.ok{{font-weight:bold}}.no{{font-weight:bold}}</style></head>
<body><h1>ResumeLens Candidate Profile</h1><h2>{escape(c.name)}</h2>
<p><b>Email:</b> {escape(c.contact.email or 'N/A')} &nbsp; <b>Phone:</b> {escape(c.contact.phone or 'N/A')}</p>
<h3>Experience</h3><ul>{experience or '<li>N/A</li>'}</ul>
<h3>Education</h3><ul>{education or '<li>N/A</li>'}</ul>
<h3>Normalized Qualifications</h3><ul>{qualifications or '<li>N/A</li>'}</ul>
<h3>Profile Classification</h3><table><tr><th>Profile</th><th>Result</th><th>Explanation</th></tr>{classifications}</table>
</body></html>'''
