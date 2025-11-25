from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI(
    title="Sentiment Analysis API",
    description="A FastAPI service using DistilBERT for sentiment classification.",
    version="1.0.0"
)

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

LABELS = ["NEGATIVE", "POSITIVE"]


class TextInput(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API is running!"}


@app.post("/predict")
def predict_sentiment(input_data: TextInput):
    inputs = tokenizer(
        input_data.text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)[0]

    confidence, label_index = torch.max(probabilities, dim=0)
    label = LABELS[label_index.item()]

    return {
        "input_text": input_data.text,
        "prediction": {
            "label": label,
            "score": round(confidence.item(), 4),
        },
    }
