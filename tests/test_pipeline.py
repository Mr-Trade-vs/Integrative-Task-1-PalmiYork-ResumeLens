from resumelens.core.pipeline import process

def test_full_stack_end_to_end():
    text = """Wednesday Addams\n3 years of experience developing web applications.\nEmail: wednesday@example.com\nTechnical Skills: JS, React.js, NodeJS, Postgres, Git."""
    result = process(text)
    full_stack = next(x for x in result.classifications if x.profile == "Full Stack Developer")
    assert full_stack.accepted
    assert "candidate" in result.dsl_text
    assert "ResumeLens Candidate Profile" in result.html
