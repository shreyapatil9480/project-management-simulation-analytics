"""Feature engineering for D09."""

import pandas as pd


FEATURE_COLUMNS = ['region', 'seasonality_index', 'discount_pct']
TARGET = "forecast_accurate"


def prepare_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Select model features and target."""
    X = df[FEATURE_COLUMNS].copy()
    for col in X.select_dtypes(include="object").columns:
        X[col] = X[col].astype("category").cat.codes
    y = df[TARGET]
    return X, y
