from pathlib import Path
import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load insurance dataset from a CSV file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at: {file_path}")

    return pd.read_csv(path)


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Apply basic cleaning and derived insurance metrics."""
    df = df.copy()

    if "TransactionMonth" in df.columns:
        df["TransactionMonth"] = pd.to_datetime(df["TransactionMonth"], errors="coerce")

    df["HasClaim"] = (df["TotalClaims"] > 0).astype(int)
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]

    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"].replace(0, pd.NA)
    df["LossRatio"] = df["LossRatio"].fillna(0)

    return df
