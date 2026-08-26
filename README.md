# fraud-scoring-platform

[![CI](https://github.com/TERK93/fraud-scoring-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/TERK93/fraud-scoring-platform/actions/workflows/ci.yml)

A small end-to-end fraud-scoring pipeline: a model trained on real historical
transaction data, serving live predictions against a continuously-generated
transaction stream.

## Why this shape

Real fraud transaction data can't be streamed live for privacy reasons, so
this project splits the same way production fraud systems do: train offline
on real, labeled historical data; score online against live traffic. Here,
"live traffic" is a generator calibrated to the training data's statistics,
since a real live feed isn't publicly available — but the ingestion,
scoring, and serving pipeline around it is real.

## Data source

[Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud),
Machine Learning Group, Université Libre de Bruxelles (ULB). 284,807
transactions, 492 frauds (0.172%), features V1–V28 (PCA-transformed) plus
Time and Amount. Licensed under DbCL-1.0 — attribution above satisfies it.
Downloaded via `kaggle datasets download -d mlg-ulb/creditcardfraud`
(requires `KAGGLE_USERNAME`/`KAGGLE_KEY` in `.env`, see `.env.example`).

## Architecture

```
Kaggle "Credit Card Fraud Detection" dataset (historical, labeled)
        |
        v
  ml/train.py  --> trained model
        |
        v
ingestion/generator.py --(live transactions)--> api/main.py (FastAPI /predict)
        |                                              |
        v                                              v
   PostgreSQL (raw + scored transactions) <----- dbt staging/marts + tests
        |
        v
   Power BI dashboard
```

## Local setup

```bash
cp .env.example .env   # fill in KAGGLE_USERNAME / KAGGLE_KEY
pip install -r requirements.txt
docker compose up -d postgres
uvicorn api.main:app --reload
```

## Testing

```bash
ruff check .
pytest -v
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for branching, PR, and review rules.
