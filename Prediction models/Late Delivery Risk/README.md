# Late Delivery Risk (Binary Classification)

**Business Question:** *Will an order be delivered late (`0 = On Time`, `1 = Late`)?*  
**Decision Supported:** Proactive flagging of high-risk orders prior to dispatch.

## Contents

- `late_delivery_risk_clean.py`: End-to-end leakage-free classification pipeline.
- `ldr_predictions.csv`: Out-of-sample test predictions (`36,104` rows) linked to Power BI via `Order Item Id`.
- `ldr_comparison.csv`: Model performance summary across Logistic Regression, Decision Tree (Base), and Decision Tree (Tuned).
- `ldr_importance.csv`: Feature importance comparison between Base and Tuned Decision Trees.
- `plots/`: 8 Matplotlib figures (Confusion Matrices, Base & Tuned Decision Tree diagrams, Feature Importance charts, and Model Comparison).
- `PowerBI_Modeling_LDR.jpg`: Power BI modeling page for Late Delivery Risk.

## Evaluation Summary (36,104 Test Orders)

| Model | Accuracy | Precision | Recall | F1 Score |
| :--- | :---: | :---: | :---: | :---: |
| Logistic Regression | 0.697 (69.7%) | 0.850 (85.0%) | 0.543 (54.3%) | 0.663 (66.3%) |
| Decision Tree (Base) | 0.697 (69.7%) | 0.849 (84.9%) | 0.544 (54.4%) | 0.663 (66.3%) |
| Decision Tree (Tuned) | 0.697 (69.7%) | 0.849 (84.9%) | 0.544 (54.4%) | 0.663 (66.3%) |

- **Tuned Confusion Matrix:** `14,396` TN | `1,912` FP | `9,032` FN | `10,764` TP.
- **Top Feature:** `Days for shipment (scheduled)` accounts for **99.79%** of splitting importance after tuning.
