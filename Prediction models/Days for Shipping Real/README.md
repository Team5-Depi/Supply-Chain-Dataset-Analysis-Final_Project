# Days for Shipping Real (Regression)

**Business Question:** *How many actual days will shipping take (`0` to `6` days, mean = `3.498`)?*  
**Decision Supported:** Improving customer delivery-time estimates and SLA planning.

## Contents

- `days_for_shipping_real_clean.py`: End-to-end leakage-free regression pipeline.
- `dfs_predictions.csv`: Out-of-sample test predictions (`36,104` rows) linked to Power BI via `Order Item Id`.
- `dfs_comparison.csv`: Model performance summary across Linear Regression, Decision Tree (Base), and Decision Tree (Tuned).
- `dfs_importance.csv`: Feature importance comparison between Base and Tuned Decision Trees.
- `plots/`: 8 Matplotlib figures (Actual vs. Predicted scatter plots, Base & Tuned Decision Tree diagrams, Feature Importance charts, and R² Comparison).
- `PowerBI_Modeling_DFS.jpg`: Power BI modeling page for Days for Shipping (Real).

## Evaluation Summary (36,104 Test Orders)

| Model | R² | MSE | MAE (Days) |
| :--- | :---: | :---: | :---: |
| Linear Regression | 0.392 | 1.602 | 0.983 |
| Decision Tree (Base) | 0.392 | 1.602 | 0.981 |
| Decision Tree (Tuned) | 0.392 | 1.602 | 0.981 |

- **Top Feature:** `Days for shipment (scheduled)` accounts for **99.84%** of importance in both Base and Tuned trees.
- **Mean Alignment:** Tuned predicted mean (`3.498` days) matches the actual test mean (`3.498` days) with zero systematic bias.
