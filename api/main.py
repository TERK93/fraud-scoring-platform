from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Fraud Scoring API")


class Transaction(BaseModel):
    transaction_id: str
    amount: float


class PredictResponse(BaseModel):
    transaction_id: str
    fraud_score: float


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(transaction: Transaction) -> PredictResponse:
    # Placeholder score until the trained model is wired in (see ml/train.py task).
    return PredictResponse(transaction_id=transaction.transaction_id, fraud_score=0.0)
