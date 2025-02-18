import pandas as pd

def normalize_ratings(df):
    df["rating"] = df["rating"] / df["rating"].max()
    return df
