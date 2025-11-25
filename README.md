# NLP Sentiment Analysis API  
### FastAPI · Hugging Face Transformers · Docker · Kubernetes (Minikube)

This project implements a **production-style NLP inference service** for sentiment analysis using a pre-trained **DistilBERT** model from Hugging Face.  
It demonstrates the end-to-end lifecycle of deploying an NLP model, including:

- FastAPI backend  
- HuggingFace Transformers  
- Docker containerization  
- Kubernetes deployment via Minikube  
- Clean local development environment  
- Interactive Swagger documentation  

---

##  Features

-  **Sentiment Classification** (Positive / Negative)  
-  FastAPI REST endpoint for inference  
-  Swagger UI automatically generated at `/docs`  
-  Reproducible Dockerized environment  
-  Kubernetes Deployment using Minikube  
-  Clean, extensible architecture  

---

##  Technologies Used

| Tool | Purpose |
|------|---------|
| **FastAPI** | Web API Framework |
| **HuggingFace Transformers** | Pretrained NLP Model |
| **PyTorch** | Model backend |
| **Docker** | Containerization |
| **Kubernetes + Minikube** | Deployment & Orchestration |
| **Uvicorn** | ASGI server |
| **Swagger UI** | API Docs |

---

##  Project Structure



nlp-sentiment-api/
│
├── main.py # FastAPI application (DistilBERT inference)
├── requirements.txt # Dependencies
├── Dockerfile # Docker build config
├── .dockerignore
├── k8s/ # Kubernetes manifests
│ ├── deployment.yaml
│ └── service.yaml
└── README.md


---

# Local Development

##  1. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate

 2. Install dependencies
pip install -r requirements.txt

 3. Run API locally
python -m uvicorn main:app --reload


Open Swagger UI:
 http://127.0.0.1:8000/docs

 Docker Deployment
 Build image
docker build -t nlp-sentiment-api .

 Run container
docker run -p 8000:8000 nlp-sentiment-api

Open the API:
 http://127.0.0.1:8000/docs

Kubernetes Deployment (Minikube)
Start Minikube
minikube start

Build Docker image inside Minikube
eval $(minikube docker-env)
docker build -t nlp-sentiment-api:latest .

Apply Kubernetes manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Access the service
minikube service sentiment-api-service --url

Then open the returned URL + /docs for interactive API documentation.

Example API Requests
Positive Example
curl -X POST "<YOUR_URL>/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this project!"}'

Negative Example
curl -X POST "<YOUR_URL>/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is terrible and disappointing."}'

Future Improvements

GitHub Actions CI/CD pipeline

Prometheus metrics + Grafana dashboard

Multilingual sentiment analysis

Unit testing (pytest)

Cloud deployment (AWS / GCP / Azure)

Author

Dariya Baigereyeva
NLP & Data Analyst | AI Practitioner

GitHub: https://github.com/DariyaB01

