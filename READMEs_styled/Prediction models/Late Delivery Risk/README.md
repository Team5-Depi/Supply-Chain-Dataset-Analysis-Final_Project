# Late Delivery Risk (Binary Classification)

Predicts whether an order will be delivered late (`0 = On Time`, `1 = Late`) prior to dispatch to support proactive flagging of high-risk orders.

[![Late Delivery Risk Power BI Modeling](PowerBI_Modeling_LDR.jpg)](PowerBI_Modeling_LDR.jpg)

## Contents

- `late_delivery_risk_clean.py`: Leakage-free classification pipeline.
- `ldr_predictions.csv`: Test-set predictions (`36,104` rows, joined to Power BI via `Order Item Id`).
- `ldr_comparison.csv`: Model comparison table across Logistic Regression, Decision Tree (Base), and Decision Tree (Tuned).
- `ldr_importance.csv`: Base vs. Tuned Decision Tree feature importances.
- `plots/`: 8 Matplotlib figures (Confusion Matrices, Base & Tuned Decision Tree diagrams, Feature Importance charts, and Model Comparison).
- `PowerBI_Modeling_LDR.jpg`: Power BI modeling page snapshot.

## Key Results (36,104 Test Orders)

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.697 (69.7%) | 0.850 (85.0%) | 0.543 (54.3%) | 0.663 (66.3%) |
| Decision Tree (Base) | 0.697 (69.7%) | 0.849 (84.9%) | 0.544 (54.4%) | 0.663 (66.3%) |
| Decision Tree (Tuned) | 0.697 (69.7%) | 0.849 (84.9%) | 0.544 (54.4%) | 0.663 (66.3%) |

- **Confusion Matrix (Tuned):** `14,396` True Negatives, `1,912` False Positives, `9,032` False Negatives, `10,764` True Positives.
- **Top Feature:** `Days for shipment (scheduled)` accounts for **99.79%** of splitting importance after tuning.

## Model Plots

[![Figure 2026-11-23 052356 (16).png](plots/Figure%202026-11-23%20052356%20%2816%29.png)](plots/Figure%202026-11-23%20052356%20%2816%29.png)

[![Figure 2026-11-23 052356 (17).png](plots/Figure%202026-11-23%20052356%20%2817%29.png)](plots/Figure%202026-11-23%20052356%20%2817%29.png)

[![Figure 2026-11-23 052356 (18).png](plots/Figure%202026-11-23%20052356%20%2818%29.png)](plots/Figure%202026-11-23%20052356%20%2818%29.png)

[![Figure 2026-11-23 052356 (19).png](plots/Figure%202026-11-23%20052356%20%2819%29.png)](plots/Figure%202026-11-23%20052356%20%2819%29.png)

[![Figure 2026-11-23 052356 (20).png](plots/Figure%202026-11-23%20052356%20%2820%29.png)](plots/Figure%202026-11-23%20052356%20%2820%29.png)

[![Figure 2026-11-23 052356 (21).png](plots/Figure%202026-11-23%20052356%20%2821%29.png)](plots/Figure%202026-11-23%20052356%20%2821%29.png)

[![Figure 2026-11-23 052356 (22).png](plots/Figure%202026-11-23%20052356%20%2822%29.png)](plots/Figure%202026-11-23%20052356%20%2822%29.png)

[![Figure 2026-11-23 052356 (23).png](plots/Figure%202026-11-23%20052356%20%2823%29.png)](plots/Figure%202026-11-23%20052356%20%2823%29.png)

