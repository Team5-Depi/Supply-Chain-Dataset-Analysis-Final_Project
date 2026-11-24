# Supply Chain Dataset Analysis & Predictive Modeling

An end-to-end Data Analytics, Data Warehousing, Business Intelligence, and Machine Learning project built on the **DataCo Smart Supply Chain** dataset (2015–2018, 180,519 order-item records).

## Repository Structure

| Folder | Description |
| :--- | :--- |
| [`Data/`](./Data) | Raw source datasets (`Original data/`) and the cleaned modeling dataset (`Cleaned data/`). |
| [`Database/`](./Database) | SQL Server Snowflake Schema backup (`Database.zip` containing `CoSupplyChain.bak`) and ERD diagram (`Database_Schema.jpg`). |
| [`Power BI/`](./Power%20BI) | Interactive Power BI workbook (`SupplyChain.pbix`), KPI snapshots, and green-themed dashboard exports (`dashboard/`). |
| [`Prediction models/`](./Prediction%20models) | Leakage-free Python ML pipelines, evaluation CSVs, Matplotlib figures, and Power BI modeling pages for three targets. |
| [`Report/`](./Report) | Analytical business questions/measures documentation and the final predictive modeling report (`.docx`). |

## Key Highlights

- **Data Engineering & Warehousing:** Cleaned 180,519 order-item records (34 columns, zero missing values) and modeled a **Snowflake Schema** in SQL Server (`fact_order_items` + 15 dimension tables).
- **Business Intelligence (Power BI):** Built a 4-page executive dashboard covering **Overview**, **Sales & Profit**, **Shipping & Cancel Rate**, and **Predictive Insights** ($36.78M Total Sales, $3.97M Profit, 12% Profit Margin, 57.33% Late Delivery Rate).
- **Predictive Modeling (Scikit-Learn):** Trained and tuned baseline linear and Decision Tree models across three targets:
  - **Late Delivery Risk** (Binary Classification): `69.7%` Accuracy, `85.0%` Precision, `66.3%` F1 Score.
  - **Days for Shipping Real** (Regression): `R² = 0.392`, `MAE = 0.981` days.
  - **Benefit per Order** (Regression): `R² = 0.024`, `MAE = $54.068` (demonstrating pre-fulfillment cost-data limits once post-facto leakage is removed).
