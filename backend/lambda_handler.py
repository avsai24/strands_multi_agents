# backend/lambda_handler.py

from agents.math_agent import math_agent

if __name__ == "__main__":
    print(math_agent("25 / 5 + 3"))
