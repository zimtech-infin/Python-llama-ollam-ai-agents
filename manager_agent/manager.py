import requests
import logging
from utils.logger import setup_logger

logger = setup_logger("manager_agent")

class ManagerAgent:
    """
    The Manager AI Agent acts as the orchestrator of all sub-agents.
    It delegates tasks to:
      - Process Verification Sub-Agent
      - Parsing Sub-Agent
    """

    def __init__(self, verifier_url=None, parser_url=None):
        self.verifier_url = verifier_url
        self.parser_url = parser_url

    def process_request(self, user_input: dict) -> dict:
        """
        Handles the entire workflow:
        1. Input verification
        2. Input parsing
        3. Aggregates results
        """
        logger.info("Starting Manager Agent Workflow...")

        # Step 1: Verify Input
        logger.info("Verifying input with Process Verifier Sub-Agent...")
        if not self.verify_input(user_input):
            logger.error("Input verification failed.")
            return {"error": "Invalid input data"}

        # Step 2: Parse Input
        logger.info("Parsing input with Parsing Sub-Agent...")
        parsed_result = self.parse_input(user_input)
        if "error" in parsed_result:
            logger.error("Parsing failed.")
            return parsed_result

        logger.info("Manager Agent Workflow completed successfully.")
        return {"parsed_data": parsed_result}

    def verify_input(self, input_data: dict) -> bool:
        """
        Calls the Process Verifier Sub-Agent to validate input.
        """
        try:
            response = requests.post(self.verifier_url, json=input_data)
            return response.json().get("valid", False)
        except Exception as e:
            logger.error(f"Process Verifier failed: {e}")
            return False

    def parse_input(self, input_data: dict) -> dict:
        """
        Calls the Parsing Sub-Agent to clean and chunk input data.
        """
        try:
            response = requests.post(self.parser_url, json=input_data)
            return response.json()
        except Exception as e:
            logger.error(f"Parsing Sub-Agent failed: {e}")
            return {"error": "Parsing failed"}
