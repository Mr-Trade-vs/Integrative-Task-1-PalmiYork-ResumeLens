from resumelens.extraction import extract

def test_extracts_resume_fields():
    text = "Ana\n3 years of experience. Email ana@example.com. Skills: JS, React.js, NodeJS, Postgres, Git."
    result = extract(text)
    assert result.candidate.name == "Ana"
    assert result.candidate.email == "ana@example.com"
    assert result.candidate.years_experience == 3
    assert set(result.candidate.qualifications) >= {"JS", "React.js", "NodeJS", "Postgres", "Git"}
