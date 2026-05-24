from src.modeling import calculate_suggested_premium


def test_calculate_suggested_premium():
    premium = calculate_suggested_premium(
        predicted_severity=1000,
        claim_probability=1,
        expense_loading=500,
        profit_margin=0.15
    )

    assert premium > 0
