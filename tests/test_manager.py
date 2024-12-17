import pytest
from unittest.mock import patch
from manager_agent.manager import ManagerAgent

def test_manager_workflow_valid():
    manager = ManagerAgent()

    input_data = {"query": "What is LLaMA2?", "user_id": 123}

    with patch.object(manager, "verify_input", return_value=True):
        with patch.object(manager, "parse_input", return_value={"clean_text": "What is LLaMA2?"}):
            result = manager.process_request(input_data)

    assert "parsed_data" in result
    assert result["parsed_data"]["clean_text"] == "What is LLaMA2?"

def test_manager_workflow_verification_failure():
    manager = ManagerAgent()
    input_data = {"query": "What is LLaMA2?", "user_id": 123}

    with patch.object(manager, "verify_input", return_value=False):
        result = manager.process_request(input_data)

    assert "error" in result
    assert result["error"] == "Invalid input data"

def test_manager_workflow_parsing_failure():
    manager = ManagerAgent()
    input_data = {"query": "What is LLaMA2?", "user_id": 123}

    with patch.object(manager, "verify_input", return_value=True):
        with patch.object(manager, "parse_input", return_value={"error": "Parsing failed"}):
            result = manager.process_request(input_data)

    assert "error" in result
    assert result["error"] == "Parsing failed"
