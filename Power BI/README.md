# Power BI Dashboard & Visuals

This folder contains the interactive Power BI report and exported visual snapshots.

## Contents

- `SupplyChain.pbix`: Main Power BI Desktop workbook connected to the Snowflake Schema and ML test-set outputs (`*_predictions.csv`, `*_comparison.csv`, `*_importance.csv`).
- `dashboard/`: Final green-themed dashboard page exports:
  - `Overview.jpg`: Executive KPIs ($36.78M Sales, $3.97M Profit, 12% Margin, 66K Orders, 21K Customers, $502.71 AOV), monthly sales trend, top products, and market/category breakdowns.
  - `Sales_and_Profit.jpg`: Regional sales/profit/cost comparison, top 10 categories by profit and sales, and customer segment distribution.
  - `Shipping_and_Cancel_Rate.jpg`: Shipping performance KPIs (2.93 avg scheduled days, 3.50 avg actual days, 57.33% late delivery rate, 0.57 avg delay days), cancel rates by category/market, and delivery status breakdown.
  - `Predictive.jpg`: Unified interactive predictive analytics page combining Late Delivery Risk and Days for Shipping Real metrics, feature importances, confusion matrix, and actual vs. predicted shipping days by mode.
- `Measures_KPIs.jpg`, `Report_Visuals.jpg`, `Modeling_Dashboard_Before.jpg`: Supporting KPI and earlier modeling layout snapshots.
