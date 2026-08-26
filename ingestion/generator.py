"""Live synthetic transaction generator.

Emits transactions shaped like the Kaggle "Credit Card Fraud Detection"
dataset (transaction_id, amount, timestamp). The amount distribution here is
a placeholder — calibrating it against data/sample/'s real distribution is
a follow-up task, not done yet.
"""

import random
import uuid
from datetime import datetime, timezone


def generate_transaction() -> dict:
    return {
        "transaction_id": str(uuid.uuid4()),
        "amount": round(random.lognormvariate(3.0, 1.2), 2),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
