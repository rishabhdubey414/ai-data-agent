from fastapi import FastAPI
from pydantic import BaseModel
from .agent import run_agent

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Query):
    answer = run_agent(q.question)
    return {"response": answer}