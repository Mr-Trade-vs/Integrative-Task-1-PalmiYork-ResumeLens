from html import escape

def render(result) -> str:
    c = result.extraction.candidate
    rows = "".join(f"<li>{escape(q)}</li>" for q in result.normalization.normalized)
    classifications = "".join(
        f"<tr><td>{escape(r.profile)}</td><td class='{('ok' if r.accepted else 'no')}'>{'ACCEPTED' if r.accepted else 'REJECTED'}</td><td>{escape(r.explanation)}</td></tr>"
        for r in result.classifications
    )
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>ResumeLens - {escape(c.name)}</title>
<style>body{{font-family:Arial,sans-serif;max-width:900px;margin:40px auto;padding:0 20px}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #ddd;padding:8px;text-align:left}}.ok{{font-weight:bold}}.no{{font-weight:bold}}</style></head>
<body><h1>ResumeLens Candidate Profile</h1><h2>{escape(c.name)}</h2>
<p><b>Email:</b> {escape(c.email or 'N/A')} &nbsp; <b>Phone:</b> {escape(c.phone or 'N/A')}</p>
<p><b>Experience:</b> {c.years_experience if c.years_experience is not None else 'N/A'} years</p>
<h3>Normalized Qualifications</h3><ul>{rows}</ul>
<h3>Profile Classification</h3><table><tr><th>Profile</th><th>Result</th><th>Explanation</th></tr>{classifications}</table>
</body></html>'''
