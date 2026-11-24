# Prediction Models

This directory contains the Python machine learning pipelines, exported test-set predictions, comparison and feature-importance CSVs, Matplotlib diagnostic plots, and Power BI modeling snapshots for all three predictive targets.

## Shared 6-Stage Leakage-Free Pipeline

All three scripts (`pandas`, `scikit-learn`, `matplotlib`) follow the same workflow on `DataCoSupplyChain_Cleaned.csv`:
1. **Feature Engineering:** Extract `order_year`, `order_month`, and `order_weekday` from `DateOrders` (omitting zero-variance `order_hour`).
2. **Train-Test Split:** 80% Training (`144,415` rows) / 20% Testing (`36,104` rows) using `random_state=42` (stratified for classification).
3. **Preprocessing:** Fit `StandardScaler` (numerical) and `OneHotEncoder(handle_unknown='ignore')` (categorical) exclusively on training data.
4. **Feature Selection:** Forward `SequentialFeatureSelector(cv=3)` selecting the top 10 features per target.
5. **Training & Tuning:** Compare a linear baseline (`LogisticRegression` / `LinearRegression`), untuned `DecisionTree`, and 3-fold `GridSearchCV` tuned `DecisionTree`.
6. **Export:** Output `*_predictions.csv`, `*_comparison.csv`, and `*_importance.csv` for Power BI.

## Target Subfolders

| Target | Problem Type | Key Results |
|---|---|---|
| [`Late Delivery Risk/`](./Late%20Delivery%20Risk) | Binary Classification | Accuracy: `69.7%`, Precision: `85.0%`, F1: `66.3%` |
| [`Days for Shipping Real/`](./Days%20for%20Shipping%20Real) | Regression | `R² = 0.392`, `MSE = 1.602`, `MAE = 0.981` days |
| [`Benefit per Order/`](./Benefit%20per%20Order) | Regression | `R² = 0.024`, `MSE = 10,037.371`, `MAE = $54.068` |
