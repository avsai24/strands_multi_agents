# backend/lambda_handler.py

from agents.orchestrator import orchestrate

if __name__ == "__main__":
    response = orchestrate("Hello, orchestrator!")
    print(response)
