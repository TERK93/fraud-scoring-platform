from ingestion.generator import generate_transaction


def test_generate_transaction_shape():
    txn = generate_transaction()
    assert set(txn.keys()) == {"transaction_id", "amount", "timestamp"}
    assert txn["amount"] > 0
