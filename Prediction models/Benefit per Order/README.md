# Benefit per Order (Regression)

Evaluates whether pre-fulfillment order attributes can predict order profitability (`-$4,274.98` to `$911.80`, mean = `$21.97`) after removing post-facto accounting leakage (`Order Item Profit Ratio`, `Order Item Total`).

[![Benefit per Order Power BI Modeling](PowerBI_Modeling_BPO.jpg)](PowerBI_Modeling_BPO.jpg)

## Contents

- `benefit_per_order_clean.py`: Leakage-free regression pipeline.
- `bpo_predictions.csv`: Test-set predictions (`36,104` rows, joined to Power BI via `Order Item Id`).
- `bpo_comparison.csv`: Model comparison table across Linear Regression, Decision Tree (Base), and Decision Tree (Tuned).
- `bpo_importance.csv`: Base vs. Tuned Decision Tree feature importances.
- `plots/`: 8 Matplotlib figures (Actual vs. Predicted scatter plots, Base & Tuned Decision Tree diagrams, Feature Importance charts, and R² Comparison).
- `PowerBI_Modeling_BPO.jpg`: Power BI modeling page snapshot.

## Key Results (36,104 Test Orders)

| Model | R² | MSE | MAE ($) |
|---|---:|---:|---:|
| Linear Regression | 0.024 | 10,037.371 | 54.068 |
| Decision Tree (Base) | -0.011 | 10,391.404 | 55.094 |
| Decision Tree (Tuned) | 0.023 | 10,046.056 | 54.058 |

- **Pruning Impact:** Tuning eliminated overfitting (`R²` improved from `-0.011` to `0.023`), shifting importance from noisy state indicators to `Sales` (**79.65%**), `Category Name_COMPUTERS` (**10.67%**), and `Order Item Discount Rate` (**7.06%**).
- **Finding:** Low `R²` (`0.024`) confirms that without unit-cost/COGS data, pre-order attributes alone cannot accurately predict net order profit.

## Model Plots

[![Figure 2026-11-23 052356 (0).png](plots/Figure%202026-11-23%20052356%20%280%29.png)](plots/Figure%202026-11-23%20052356%20%280%29.png)

[![Figure 2026-11-23 052356 (1).png](plots/Figure%202026-11-23%20052356%20%281%29.png)](plots/Figure%202026-11-23%20052356%20%281%29.png)

[![Figure 2026-11-23 052356 (2).png](plots/Figure%202026-11-23%20052356%20%282%29.png)](plots/Figure%202026-11-23%20052356%20%282%29.png)

[![Figure 2026-11-23 052356 (3).png](plots/Figure%202026-11-23%20052356%20%283%29.png)](plots/Figure%202026-11-23%20052356%20%283%29.png)

[![Figure 2026-11-23 052356 (4).png](plots/Figure%202026-11-23%20052356%20%284%29.png)](plots/Figure%202026-11-23%20052356%20%284%29.png)

[![Figure 2026-11-23 052356 (5).png](plots/Figure%202026-11-23%20052356%20%285%29.png)](plots/Figure%202026-11-23%20052356%20%285%29.png)

[![Figure 2026-11-23 052356 (6).png](plots/Figure%202026-11-23%20052356%20%286%29.png)](plots/Figure%202026-11-23%20052356%20%286%29.png)

[![Figure 2026-11-23 052356 (7).png](plots/Figure%202026-11-23%20052356%20%287%29.png)](plots/Figure%202026-11-23%20052356%20%287%29.png)

