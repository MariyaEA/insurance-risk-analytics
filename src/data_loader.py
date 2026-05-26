from pathlib import Path
import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load insurance dataset from a CSV file with basic validation."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at: {file_path}")

    if path.suffix.lower() != ".csv":
        raise ValueError("Input file must be a CSV file.")

    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("Loaded dataset is empty.")

    return df


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Apply basic cleaning and derived insurance metrics."""
    if df is None:
        raise ValueError("Input dataframe cannot be None.")

    if df.empty:
        raise ValueError("Input dataframe is empty.")

    required_cols = ["TotalPremium", "TotalClaims"]

    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        raise KeyError(f"Missing required columns: {missing_cols}")

    df = df.copy()

    if "TransactionDate" in df.columns:
        df["TransactionDate"] = pd.to_datetime(
            df["TransactionDate"],
            errors="coerce"
        )

    df["HasClaim"] = (df["TotalClaims"] > 0).astype(int)
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]

    df["LossRatio"] = (
        df["TotalClaims"] /
        df["TotalPremium"].replace(0, pd.NA)
    )

    df["LossRatio"] = df["LossRatio"].fillna(0)

    return df
