# Presentation

This directory contains the final graduation project presentation deck, styled in the project's green-and-gold Power BI theme.

## Contents

- `Supply_Chain_Dataset_Analysis_Presentation.pptx`: 15-slide executive presentation covering:
  1. **Cover:** Project title, Team 5 (Mind Readers), ITC & DEPI logos, and custom supply chain illustration.
  2. **Mind Readers Team:** Team roster and leadership.
  3. **Business Problem & Objectives:** Core sales, shipping SLA, cancellation, and predictive goals.
  4. **Dataset Overview:** Raw (53 cols) → Cleaned (34 cols, 180,519 rows, 0 nulls) across 164 countries.
  5. **Selected Domain Variables:** Order, Shipping, Destination, Customer & Product, and Financial domains.
  6. **Project Workflow:** 6-stage end-to-end execution across team members.
  7. **SQL Server Database Design:** `stg_dataco`, `fact_order_items`, and 18 normalized dimensions.
  8. **Snowflake Schema:** Full Entity-Relationship Diagram.
  9. **Data Preparation, Measures & Ticker:** Profiling summary, moving ticker, and core DAX KPIs.
  10. **Predictive Modeling (3 Targets):** 6-stage leakage-free pipeline, `84.9%` Precision (`Late Delivery Risk`), `R² = 0.392` (`Days for Shipping Real`), and `R² = 0.023` (`Benefit per Order`).
  11. **Predictive Modeling (Model Comparison):** Combined comparison table of the evaluated models across the three targets, noting that additional algorithms (Random Forest, Gradient Boosting) were evaluated and the presented models remained the best choice.
  12. **Dashboard Overview & Web App:** 4-page green-and-gold Power BI dashboard and bilingual HTML web app.
  13. **Insights & Recommendations:** SLA recalibration, cancellation hotspots, top profit drivers, and early-warning alerts.
  14. **Conclusion:** SQL Server + Python ML + Web App + Power BI + DAX summary.
  15. **Thank You:** Closing Q&A slide.
