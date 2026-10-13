from resumelens.core.pipeline import process

def test_full_stack_end_to_end():
    text = """Wednesday Addams\n3 years of experience developing web applications.\nEmail: wednesday@example.com\nTechnical Skills: JS, React.js, NodeJS, Postgres, Git."""
    result = process(text)
    full_stack = next(x for x in result.classifications if x.profile == "Full Stack Developer")
    assert full_stack.accepted
    assert "candidate" in result.dsl_text
    assert 'skill "JAVASCRIPT";' in result.dsl_text
    assert 'skill "JS";' not in result.dsl_text
    assert "ResumeLens Candidate Profile" in result.html
    assert "missing required qualifications" in result.html


def test_pipeline_validates_and_escapes_candidate_name_for_html():
    result = process('<script>alert("x")</script>\nSkills: JS.')

    assert "&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;" in result.html
    assert "<h2><script>" not in result.html
