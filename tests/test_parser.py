import pytest
from sub_agents.parser.parser import Parser

def test_preprocess_input():
    parser = Parser()
    text = "   What   is    LLaMA2?   "
    result = parser.preprocess(text)
    assert result["clean_text"] == "What is LLaMA2?"

def test_chunk_text_small_input():
    parser = Parser()
    text = "LLaMA2 is a language model. It is efficient and optimized for modern hardware."
    chunks = parser.chunk_text(text, chunk_size=50)
    assert len(chunks) == 1
    assert "LLaMA2 is a language model" in chunks[0]

def test_chunk_text_large_input():
    parser = Parser()
    text = " ".join([f"Sentence {i}." for i in range(1, 21)])  # 20 sentences
    chunks = parser.chunk_text(text, chunk_size=50)
    assert len(chunks) > 1
    assert all(len(chunk.split()) <= 50 for chunk in chunks)
