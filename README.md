# Project Management Simulation Analytics

When do sales forecasts miss accuracy targets?

**Stakeholder:** Revenue Operations Analyst

## Key Insights

- Discounts above 20% degrade forecast accuracy in Q4.
- High seasonality regions need separate forecast models.
- West region forecasts are accurate 68% of the time at baseline.

## Dataset

Primary file: `data/sales_forecast.csv`  
Target variable: `forecast_accurate`

## Getting Started

```bash
pip install -r requirements.txt
jupyter notebook notebooks/case_study.ipynb
```


## Next Steps

**Done.** Class-weight tuning and SHAP explainability are implemented — see ### Implemented below.

---
*Analytics portfolio project — 2025-09*

<!-- build 5 -->

### Implemented

```bash
pip install -r requirements.txt
python src/train.py && python src/explain.py
```