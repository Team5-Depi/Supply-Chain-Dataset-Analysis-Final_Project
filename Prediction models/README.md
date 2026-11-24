# Prediction Models

This folder contains the machine learning pipelines, exported evaluation tables, diagnostic plots, and Power BI modeling pages for all three predictive targets.

## Modeling Pipeline (Leakage-Free 6-Stage Workflow)

All three pipelines share an identical preprocessing and evaluation structure implemented in Python (`pandas`, `scikit-learn`, `matplotlib`):
1. **Feature Engineering:** Extracted `order_year`, `order_month`, and `order_weekday` from `DateOrders` (omitting zero-variance `order_hour`).
2. **Train-Test Split:** 80% Training (`144,415` rows) / 20% Testing (`36,104` rows) with `random_state=42` (stratified for classification).
3. **Preprocessing:** `StandardScaler` on numerical features and `OneHotEncoder(handle_unknown='ignore')` on categorical features, fitted exclusively on the training set.
4. **Feature Selection:** Forward `SequentialFeatureSelector(cv=3)` selecting the top 10 predictors per target.
5. **Model Training & Tuning:** Linear baseline (`LogisticRegression` / `LinearRegression`), untuned `DecisionTree`, and 3-fold `GridSearchCV` tuned `DecisionTree`.
6. **Export:** Standardized CSVs (`*_predictions.csv`, `*_comparison.csv`, `*_importance.csv`) for Power BI integration.

## Target Subfolders

| Target Folder | Problem Type | Key Metric |
| :--- | :--- | :--- |
| [`Late Delivery Risk/`](./Late%20Delivery%20Risk) | Binary Classification | Accuracy: `69.7%`, Precision: `85.0%`, F1: `66.3%` |
| [`Days for Shipping Real/`](./Days%20for%20Shipping%20Real) | Regression | `R² = 0.392`, `MSE = 1.602`, `MAE = 0.981` days |
| [`Benefit per Order/`](./Benefit%20per%20Order) | Regression | `R² = 0.024`, `MSE = 10,037.37`, `MAE = $54.07` |
