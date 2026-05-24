import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error, r2_score


def evaluate_regression_model(model, X_test, y_test) -> dict:
    """Evaluate regression model using RMSE and R-squared."""

    predictions = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    return {
        "rmse": rmse,
        "r2": r2
    }


def create_model_results_table(results: list) -> pd.DataFrame:
    """Create a clean model comparison table."""

    return pd.DataFrame(results).sort_values("RMSE")


def calculate_suggested_premium(
    predicted_severity,
    claim_probability=1.0,
    expense_loading=500,
    profit_margin=0.15
):
    """Calculate risk-based suggested premium."""

    base_risk_cost = claim_probability * predicted_severity

    suggested_premium = (
        base_risk_cost + expense_loading
    ) * (1 + profit_margin)

    return suggested_premium