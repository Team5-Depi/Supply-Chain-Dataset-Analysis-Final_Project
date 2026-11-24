# Power BI & Dashboard

This directory contains the Power BI Desktop workbook and visual exports of the green-themed executive dashboard.

[![Supply Chain Dashboard Overview](<dashboard/Overview.jpg>)](<dashboard/Overview.jpg>)

## Contents

- `SupplyChain.pbix`: Interactive Power BI workbook built on the Snowflake Schema and linked to the ML test-set outputs (`ldr_predictions.csv`, `dfs_predictions.csv`, `bpo_predictions.csv`, plus comparison and feature-importance tables).
- `dashboard/`: Final green-themed dashboard page screenshots:
  - `Overview.jpg`: Executive KPIs (`36.78M` Total Sales, `3.97M` Total Profit, `12%` Profit Margin, `66K` Orders, `21K` Customers, `502.71` Avg Order Value) and sales breakdowns.
  - `Sales_and_Profit.jpg`: Regional sales/profit/cost comparison, Top 10 categories by profit and sales, and segment share.
  - `Shipping_and_Cancel_Rate.jpg`: Shipping and cancellation KPIs (`2.93` avg scheduled days, `3.50` avg shipping days, `57.33%` late delivery rate, `0.57` avg delay days, `0.02` cancel rate) and mode/market breakdowns.
  - `Predictive.jpg`: Unified predictive analytics page combining Late Delivery Risk and Days for Shipping Real KPIs, feature importances, confusion matrix, and actual vs. predicted shipping days by mode.
- `Measures_KPIs.jpg`, `Report_Visuals.jpg`, `Modeling_Dashboard_Before.jpg`: Supporting KPI cards and earlier modeling page snapshots.
