from nltk.tokenize import word_tokenize, sent_tokenize

class Parser:
    """
    Sub-Agent for text preprocessing: tokenizing, chunking, and cleaning.
    """

    def preprocess(self, text: str) -> dict:
        clean_text = " ".join(word for word in text.split())
        return {"clean_text": clean_text}

    def chunk_text(self, text: str, chunk_size=512) -> list:
        sentences = sent_tokenize(text)
        chunks = []
        chunk = []

        for sentence in sentences:
            if len(" ".join(chunk + [sentence])) > chunk_size:
                chunks.append(" ".join(chunk))
                chunk = [sentence]
            else:
                chunk.append(sentence)
        chunks.append(" ".join(chunk))

        return chunks
