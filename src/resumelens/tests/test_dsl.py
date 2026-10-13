import pytest
from resumelens.dsl.generator import generate
from resumelens.core.models import Candidate, ClassificationResult
from resumelens.dsl.parser import CandidateProfileValidationError, validate


def test_generator_produces_expected_structure():
    candidate = Candidate(name="Test", email="test@example.com", phone="12345678", years_experience=2, qualifications=["Python"])
    result = ClassificationResult("Data Scientist", True, ["PYTHON"], "ok")
    dsl = generate(candidate, [result], ["PYTHON"])
    assert dsl.startswith('candidate "Test"')
    assert 'skill "PYTHON";' in dsl
    assert 'classification Data_Scientist ACCEPTED "ok";' in dsl
    model = validate(dsl)
    assert model.candidate.classification[0].explanation == "ok"


def test_generated_dsl_is_valid_and_escapes_special_characters():
    candidate = Candidate(name='Ana "Annie" \\ Gómez', email="ana@example.com")
    dsl = generate(candidate, [], ["C++", "SCIKIT_LEARN"])

    model = validate(dsl)

    assert model.candidate.name == candidate.name
    assert [item.value for item in model.candidate.skill] == ["C++", "SCIKIT_LEARN"]
    assert model.candidate.classification == []


def test_invalid_dsl_is_rejected():
    with pytest.raises(CandidateProfileValidationError, match="does not match the DSL grammar"):
        validate('candidate "Missing contact" { skill "PYTHON"; }')


def test_textx_validation_when_installed():
    pytest.importorskip("textx")
    model = validate('''candidate "Test" { contact { "test@example.com" "12345678" } experience "Acme" "Engineer" 2; skill "Python"; classification Data_Scientist ACCEPTED; }''')
    assert model.candidate.name == "Test"
