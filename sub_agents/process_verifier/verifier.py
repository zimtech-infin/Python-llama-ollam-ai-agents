from pydantic import BaseModel, ValidationError

class QueryInput(BaseModel):
    query: str
    user_id: int

class ProcessVerifier:
    """
    Sub-Agent responsible for verifying input data integrity.
    """

    def validate_input(self, input_data):
        try:
            validated = QueryInput(**input_data)
            return {"valid": True, "message": "Input is valid"}
        except ValidationError as e:
            return {"valid": False, "message": str(e)}
