# 🚀 NLP Sentiment Analysis API  
### FastAPI · Hugging Face Transformers · Docker · Kubernetes (Minikube)

This project implements a **production-style NLP inference service** for sentiment analysis using a pre-trained **DistilBERT** model from Hugging Face.  
It demonstrates the end-to-end lifecycle of deploying an NLP model, including:

- ⚡ FastAPI backend  
- 🤗 HuggingFace Transformers  
- 🐳 Docker containerization  
- ☸️ Kubernetes deployment via Minikube  
- 📦 Local development environment  
- 🧪 Interactive Swagger documentation  

Perfect for demonstrating **NLP, MLOps, and deployment skills**.

---

# 📌 Features

- 🔍 **Sentiment Classification** (Positive / Negative)  
- 🚀 **FastAPI** REST endpoint for inference  
- 📘 **Swagger UI** automatically generated at `/docs`  
- 🐳 **Dockerized** for reproducible environments  
- ☸️ **Kubernetes Deployment** using Minikube  
- 💡 Clean, extensible project structure  

---

# 🧠 Technologies Used

| Tool | Purpose |
|------|---------|
| **FastAPI** | Web API Framework |
| **Transformers (Hugging Face)** | Pretrained NLP Model |
| **PyTorch** | Model backend |
| **Docker** | Containerization |
| **Kubernetes + Minikube** | Local deployment & orchestration |
| **Uvicorn** | ASGI server |
| **curl / Swagger UI** | Testing API |

---

# Project Structure

nlp-sentiment-api/
│
├── main.py # FastAPI application with sentiment analysis
├── requirements.txt # Dependencies
├── Dockerfile # Containerization
├── .dockerignore
├── k8s/
│ ├── deployment.yaml # Kubernetes Deployment
│ └── service.yaml # Kubernetes Service
└── README.md


---

# Local Development

### 1. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python -m uvicorn main:app --reload
Open Swagger documentation:
http://127.0.0.1:8000/docs

### 2. Docker deployment
docker build -t nlp-sentiment-api .
docker run -p 8000:8000 nlp-sentiment-api
Open the API:
http://127.0.0.1:8000/docs

### 3.Kubernetes deployment
minikube start
eval $(minikube docker-env)
docker build -t nlp-sentiment-api:latest .
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
minikube service sentiment-api-service --url



