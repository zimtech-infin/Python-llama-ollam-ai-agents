import pytest
from task_workers.tokenizer_worker import tokenize_text

def test_tokenize_text():
    text = "LLaMA2 is an advanced model."
    tokens = tokenize_text(text)
    assert tokens == ["LLaMA2", "is", "an", "advanced", "model"]

def test_tokenize_empty_text():
    text = ""
    tokens = tokenize_text(text)
    assert tokens == []
