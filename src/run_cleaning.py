import pandas as pd

from feature_engineering import clean_dataset

df = pd.read_csv("data/insurance_data.csv")

clean_df = clean_dataset(df)

clean_df.to_csv(
    "data/insurance_data_cleaned.csv",
    index=False
)
