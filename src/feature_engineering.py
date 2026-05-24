import pandas as pd


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Perform dataset cleaning."""

    df = df.copy()

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    categorical_cols = df.select_dtypes(include="object").columns

    for col in categorical_cols:
        df[col] = df[col].fillna("Unknown")

    return df
