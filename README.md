# **Manager AI Agent with Sub-Agents: Real-World Application in Modular AI Workflows**

## **Abstract**

This project presents an **AI Manager Agent system** that orchestrates a modular set of **sub-agents** performing distinct tasks like input validation, data preprocessing, and retrieval-augmented generation (RAG). The architecture leverages Python, Docker, and popular libraries like LlamaIndex, Ollama (for LLaMA2 models), and Pytest for robust testing. This system is designed to mirror a **real-world corporate organizational structure** with managers, supervisors, and workers. A practical application in **customer support automation** is explored to demonstrate the system's versatility and real-world efficiency.

---

## **1. Introduction**

### **1.1 Motivation**
The AI industry increasingly demands modular and scalable systems to handle complex workflows. Traditional monolithic AI models lack flexibility, maintainability, and scalability. Inspired by the hierarchical structure of modern businesses, this project implements a system where **Manager Agents** act as orchestrators, delegating tasks to specialized **Sub-Agents**. Each sub-agent focuses on distinct operations, enabling concurrent execution, modular testing, and resource efficiency.

### **1.2 Project Overview**
This system consists of:
- **Manager AI Agent**: Central orchestrator of tasks and sub-agents.
- **Sub-Agents**:
    - **Process Verification Sub-Agent**: Validates user inputs and model outputs.
    - **Parsing Sub-Agent**: Preprocesses and chunks input data.
- **Task Workers**: Perform granular tasks such as text tokenization, chunking, and query validation.
- **Integration with LLaMA2**: Uses Ollama to serve the LLaMA2 language model.
- **Testing Framework**: Unit tests using Pytest for robustness.

This project introduces a modular AI architecture with broad applicability across industries such as **customer support**, **document retrieval**, and **intelligent chatbots**.

---

## **2. System Design and Architecture**

### **2.1 Business-Inspired Structure**
The project models an AI workflow after a corporate organization:

| Business Role               | AI System Component           | Responsibilities                          |
|-----------------------------|--------------------------------|------------------------------------------|
| **CEO**                     | **Manager AI Agent**          | Orchestrates the entire workflow.        |
| **Department Managers**     | **Sub-Agent Managers**        | Oversee validation and parsing tasks.    |
| **Supervisors**             | **Sub-Agents**               | Delegate tasks to workers.               |
| **Workers**                 | **Task Executors**            | Perform specific, focused operations.    |

The **Manager AI Agent** acts as the CEO, delegating specialized tasks to sub-agents, which then coordinate with low-level task workers. This design ensures scalability, maintainability, and optimized performance.

### **2.2 Key Components**

#### **2.2.1 Manager AI Agent**
- Centralized orchestrator.
- Delegates input validation to the **Process Verification Sub-Agent**.
- Delegates input preprocessing to the **Parsing Sub-Agent**.
- Aggregates results and sends them to downstream systems (e.g., model inference).

#### **2.2.2 Process Verification Sub-Agent**
- Ensures inputs adhere to a defined schema (using Pydantic).
- Verifies the integrity and correctness of outputs.
- Prevents invalid inputs from reaching downstream components, saving computational resources.

#### **2.2.3 Parsing Sub-Agent**
- Preprocesses textual inputs:
    - Removes extraneous whitespace and punctuation.
    - Tokenizes text into manageable units.
    - Chunks large documents into smaller segments for efficient processing.

#### **2.2.4 Task Workers**
- **Query Validator**: Ensures input queries are clean and structured.
- **Tokenizer Worker**: Splits text into tokens for easier processing.
- **Quality Checker**: Validates output integrity.

### **2.3 Real-World Application**
This project is demonstrated in the context of a **Customer Support Automation System**. The AI Manager Agent handles user queries, ensuring inputs are validated, preprocessed, and sent to the LLaMA2 model for intelligent responses.

---

## **3. Real-World Application: Customer Support Automation**

### **3.1 Problem Statement**
Customer support teams handle thousands of repetitive queries daily, often leading to increased response time, human errors, and operational inefficiencies. By automating this process using an AI system, organizations can improve **response time**, **accuracy**, and **customer satisfaction**.

### **3.2 Proposed Solution**
Using the **Manager AI Agent** system:
1. The **Manager Agent** orchestrates the workflow for customer queries.
2. **Process Verification Sub-Agent** validates query inputs:
   - Checks for missing details (e.g., incomplete sentences, invalid formats).
   - Ensures the query structure aligns with predefined rules.
3. **Parsing Sub-Agent** preprocesses queries:
   - Tokenizes user input (e.g., "Order not delivered") into manageable text.
   - Chunks larger queries into smaller parts for processing.
4. The validated and preprocessed query is sent to the **LLaMA2 model** (via Ollama) to generate a relevant response.
5. Outputs are validated again to ensure clarity and relevance.

---

### **3.3 Workflow Example**
#### **Input Query**:
```
"Hi, I ordered a package last week, but it hasn't arrived yet. Can you check the status?"
```

#### **Step-by-Step Workflow**:
1. **Manager AI Agent**:
   - Delegates the query to the Process Verification Sub-Agent.

2. **Process Verification Sub-Agent**:
   - Verifies that the input query is not empty and has valid formatting.

3. **Parsing Sub-Agent**:
   - Preprocesses the query by cleaning and tokenizing it into:
     ```
     ["ordered", "package", "last week", "not arrived", "check status"]
     ```

4. **LLaMA2 Inference (via Ollama)**:
   - The query is sent to LLaMA2, which generates the following response:
     ```
     "Thank you for reaching out. Your package is currently delayed due to weather conditions. It is expected to arrive in 2 days."
     ```

5. **Process Verification Sub-Agent**:
   - Checks the response for clarity and accuracy.

6. **Final Response**:
```
"Thank you for reaching out. Your package is currently delayed due to weather conditions. It is expected to arrive in 2 days."
```

---

## **4. Implementation**

### **4.1 Technology Stack**
| Component                          | Technology Used                 |
|------------------------------------|---------------------------------|
| **Programming Language**           | Python 3.11                     |
| **Orchestration**                  | Docker, Docker Compose          |
| **Model Serving**                  | Ollama (LLaMA2)                 |
| **Data Retrieval**                 | LlamaIndex                      |
| **Input Validation**               | Pydantic                        |
| **Testing Framework**              | Pytest                          |

### **4.2 Project Directory Structure**
```
llama-index-python-ai-agent/
├── manager_agent/
├── sub_agents/
│   ├── process_verifier/
│   ├── parser/
├── task_workers/
├── tests/
│   ├── test_manager.py
│   ├── test_parser.py
│   ├── test_process_verifier.py
│   └── integration_tests.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

### **4.3 Key Modules**
#### **Manager AI Agent**
Responsible for orchestrating tasks:
```python
manager = ManagerAgent(verifier_url, parser_url)
result = manager.process_request({"query": "Track my order status", "user_id": 123})
```

#### **Process Verification**
Validates inputs and outputs:
```python
class ProcessVerifier:
    def validate_input(self, input_data):
        return {"valid": True, "message": "Input is valid."}
```

#### **Parsing Sub-Agent**
Preprocesses text:
```python
class Parser:
    def preprocess(self, text):
        return " ".join(text.split())
```

---

## **5. Testing and Validation**

Unit tests ensure system robustness. Key test cases include:
- Input validation edge cases.
- Parsing correctness for large inputs.
- Integration testing between Manager Agent and sub-agents.

Example Test:
```python
from manager_agent.manager import ManagerAgent

def test_manager_workflow():
    manager = ManagerAgent()
    input_data = {"query": "Where is my order?", "user_id": 123}
    result = manager.process_request(input_data)
    assert "parsed_data" in result
```

---

## **6. Conclusion**

The **Manager AI Agent system** offers a scalable, modular, and efficient solution for real-world workflows like customer support automation. By leveraging Python, Docker, and LLaMA2, this project demonstrates a clean and maintainable architecture that reduces complexity and improves scalability.

This structure can be adapted to various domains, including **document processing**, **enterprise chatbots**, and **retrieval-augmented AI systems**.

---

## **7. Future Work**

- **Advanced Sub-Agents**: Implement advanced agents for document summarization and semantic analysis.
- **Dynamic Scaling**: Integrate Kubernetes for auto-scaling in production environments.
- **Model Optimization**: Experiment with smaller, quantized LLaMA2 models for low-resource deployment.

---

## **8. References**
1. LLaMA2: Meta's Open-Source Language Model - [Meta AI Research](https://ai.meta.com/llama)
2. Python for AI Workflows: [Python.org](https://www.python.org)
3. LlamaIndex for Retrieval-Augmented Generation: [LlamaIndex Documentation](https://www.llamaindex.ai)
4. Docker and Containerization: [Docker Documentation](https://www.docker.com)


