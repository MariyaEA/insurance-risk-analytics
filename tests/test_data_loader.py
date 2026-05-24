import pandas as pd

from src.data_loader import basic_cleaning


def test_basic_cleaning_adds_metrics():
    df = pd.DataFrame(
        {
            "TotalPremium": [1000, 2000],
            "TotalClaims": [0, 500],
        }
    )

    cleaned = basic_cleaning(df)

    assert "HasClaim" in cleaned.columns
    assert "Margin" in cleaned.columns
    assert "LossRatio" in cleaned.columns
    assert cleaned.loc[0, "HasClaim"] == 0
    assert cleaned.loc[1, "HasClaim"] == 1
