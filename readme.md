# AI Data Agent (Ollama + FastAPI + Docker + CI/CD)

A lightweight AI agent that analyzes structured datasets and generates natural-language business insights using a local open-source LLM served via Ollama.

## 🚀 Features

* Query structured datasets (CSV)
* Automated data analysis with Pandas
* Local LLM inference via Ollama (phi-3)
* REST API with FastAPI
* Dockerized deployment
* GitHub Actions CI/CD pipeline

## 🧠 Architecture

User Query → FastAPI → Pandas Analysis → Ollama LLM → Insight Response

## 📊 Dataset

Retail sales dataset containing orders, profit, category, state, and quantity fields.

## 🐳 Run with Docker

```bash
docker build -t ai-data-agent .
docker run -p 8000:8000 ai-data-agent
```

Open: http://localhost:8000/docs

## ⚙️ CI/CD

GitHub Actions automatically builds and tests the Docker container on every push.

## 🧾 Example Query

```json
{"question":"total profit"}
```

## 🛠 Tech Stack

Python, FastAPI, Pandas, Ollama, Docker, GitHub Actions

## 📌 Author

Rishabh Raj Dubey
