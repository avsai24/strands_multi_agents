from strands import Agent, tool

@tool
def calculator(query: str) -> str:
    try:
        # Replace eval for safe parser in production!
        result = eval(query)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

@tool
def math_agent(query: str) -> str:
    agent = Agent(
        tools=[calculator],
        system_prompt="You're a math problem solver."
    )
    return agent(query)
