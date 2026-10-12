from resumelens.extraction import extract

def test_extracts_resume_fields():
    text = "Ana\n3 years of experience. Email ana@example.com. Skills: JS, React.js, NodeJS, Postgres, Git."
    result = extract(text)
    assert result.candidate.name == "Ana"
    assert result.candidate.email == "ana@example.com"
    assert result.candidate.years_experience == 3
    assert set(result.candidate.qualifications) >= {"JS", "React.js", "NodeJS", "Postgres", "Git"}

def test_special_characters_in_name():
    text = """
    Carlos
    Programming languages: C++, C#, Python.
    """
    result = extract(text)
    assert result.candidate.name == "Carlos"
    assert set(result.candidate.qualifications) >= {"C++", "C#", "Python"}

def test_false_positive_extraction():
    text = """
    Ana
    Skills: Express.js, JavaScript.
    """
    result = extract(text)
    assert result.candidate.name == "Ana"
    assert set(result.candidate.qualifications) == {"Express.js", "JavaScript"}
    assert "JS" not in result.candidate.qualifications

def test_experience_extraction_with_plus_sign():
    text = "John Doe\n5+ years of experience in software development."
    result = extract(text)
    assert result.candidate.name == "John Doe"
    assert result.candidate.years_experience == 5
    assert "5 years of experience" in result.candidate.experiences

def test_repeated_qualifications_are_unique():
    text = "Jane Smith\nSkills: Python, Django, Python, Flask."
    result = extract(text)
    assert result.candidate.name == "Jane Smith"
    assert set(result.candidate.qualifications) == {"Python", "Django", "Flask"}

def test_email_and_phone_extraction():
    text = """
    Bob Johnson
    Email: bob@example.com
    Phone: +1-555-123-4567
    """
    result = extract(text)
    assert result.candidate.name == "Bob Johnson"
    assert result.candidate.email == "bob@example.com"
    assert result.candidate.phone == "+1-555-123-4567"

def test_extracts_months_of_experience():
    text = """
    Laura
    8 months of experience developing web applications.
    """

    result = extract(text)

    assert result.candidate.years_experience is None

def test_extracts_days_of_experience():
    text = """
    Andres
    20 days of experience assisting with database migration.
    """

    result = extract(text)

    assert result.candidate.years_experience is None

def test_graduation_year_is_not_experience():
    text = """
    Natalia
    Graduated in 2022.
    Skills: Python and Git.
    """

    result = extract(text)

    assert result.candidate.years_experience is None
