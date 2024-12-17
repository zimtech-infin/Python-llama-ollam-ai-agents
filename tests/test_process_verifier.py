import pytest
from sub_agents.process_verifier.verifier import ProcessVerifier

def test_validate_input_valid():
    verifier = ProcessVerifier()
    input_data = {"query": "What is AI?", "user_id": 123}
    result = verifier.validate_input(input_data)
    assert result["valid"] is True
    assert "Input is valid" in result["message"]

def test_validate_input_invalid():
    verifier = ProcessVerifier()
    input_data = {"query": 12345, "user_id": "not_a_number"}
    result = verifier.validate_input(input_data)
    assert result["valid"] is False
    assert "ValidationError" in result["message"]

def test_validate_input_missing_key():
    verifier = ProcessVerifier()
    input_data = {"user_id": 123}
    result = verifier.validate_input(input_data)
    assert result["valid"] is False
    assert "ValidationError" in result["message"]
