from .data_loader import load_data
from .analysis import analyze
from .llm_client import ask_llm

def run_agent(user_query: str):
    df = load_data()

    structured_result = analyze(df, user_query)

    prompt = f"""
    User question: {user_query}
    Data analysis result: {structured_result}

    Explain insights in simple business language.
    """

    llm_response = ask_llm(prompt)

    return llm_response