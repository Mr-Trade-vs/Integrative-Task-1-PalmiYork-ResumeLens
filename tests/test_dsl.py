import pytest
from resumelens.dsl.generator import generate
from resumelens.core.models import Candidate, ClassificationResult


def test_generator_produces_expected_structure():
    candidate = Candidate(name="Test", email="test@example.com", phone="12345678", years_experience=2, qualifications=["Python"])
    result = ClassificationResult("Data Scientist", True, ["PYTHON"], "ok")
    dsl = generate(candidate, [result])
    assert dsl.startswith('candidate "Test"')
    assert 'skill "Python";' in dsl
    assert 'classification Data_Scientist ACCEPTED;' in dsl


def test_textx_validation_when_installed():
    parser = pytest.importorskip("textx")
    from resumelens.dsl.parser import validate
    model = validate('''candidate "Test" { contact "test@example.com" "12345678" experience "Acme" "Engineer" 2; skill "Python"; classification Data_Scientist ACCEPTED; }''')
    assert model.candidate.name == "Test"
