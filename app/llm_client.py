import requests

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

def ask_llm(prompt: str):
    payload = {
    "model": "phi3",
    "prompt": prompt,
    "stream": False
}

    r = requests.post(OLLAMA_URL, json=payload)

    print("OLLAMA STATUS:", r.status_code)
    print("OLLAMA JSON:", r.text)

    data = r.json()
    return data.get("response", "LLM error: no response field")