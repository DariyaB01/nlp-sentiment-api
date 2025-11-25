# NLP Sentiment Analysis API  
### FastAPI · Hugging Face Transformers · Docker · Kubernetes (Minikube)

This repository contains a **sentiment analysis API** built with FastAPI and a pre-trained **DistilBERT** model from Hugging Face.  
The goal of the project is to show how an NLP model can be taken from experimentation to deployment using:

- a lightweight web API (FastAPI)  
- transformer-based NLP models (Hugging Face)  
- Docker containers  
- Kubernetes (Minikube) for orchestration  

---

##  Features

- Binary **sentiment classification**: `POSITIVE` / `NEGATIVE`  
- FastAPI prediction endpoint at `/predict`  
- Interactive API docs at `/docs` (Swagger UI)  
- Reproducible Docker image for the service  
- Kubernetes Deployment & Service manifests  
- Simple structure that can be extended with more NLP tasks  

---

## Technologies Used

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-222222?style=for-the-badge&logo=uvicorn&logoColor=white)
![Transformers](https://img.shields.io/badge/Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Minikube](https://img.shields.io/badge/Minikube-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)

---

## Project Structure

```text
nlp-sentiment-api/
│
├── main.py                # FastAPI application (DistilBERT inference)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker build config
├── .dockerignore
├── k8s/                   # Kubernetes manifests
│   ├── deployment.yaml
│   └── service.yaml
└── README.md

### • Source Code: [Visit Repo](https://github.com/DariyaB01/nlp-sentiment-api)

NLP & Data Analyst | AI Practitioner

GitHub: https://github.com/DariyaB01

