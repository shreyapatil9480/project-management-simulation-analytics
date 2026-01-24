"""SHAP explainability report for trained model."""

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import shap

from features import prepare_features

DATA_PATH = Path("data/sales_forecast.csv")
MODEL_PATH = Path("models/model.joblib")
OUTPUT_PATH = Path("reports/shap_summary.png")


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    X, _ = prepare_features(df)
    model = joblib.load(MODEL_PATH)
    clf = model.named_steps.get("clf", model)
    explainer = shap.Explainer(clf, X)
    shap_values = explainer(X.iloc[: min(50, len(X))])
    shap.summary_plot(shap_values, X.iloc[: min(50, len(X))], show=False)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=120)
    plt.close()
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
