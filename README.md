# Supply Chain Dataset Analysis & Predictive Modeling Dashboard

An end-to-end supply chain analytics, data warehousing, business intelligence, and machine learning project built with SQL Server, Microsoft Power BI, and Python (Scikit-learn) to analyze sales, profitability, shipping delays, order cancellations, and predictive risk modeling on the **DataCo Smart Supply Chain** dataset (2015–2018).

[![Supply Chain Dashboard Overview](Power%20BI/dashboard/Overview.jpg)](Power%20BI/dashboard/Overview.jpg)

## Business Problem

Supply chain and e-commerce operations require clear visibility into sales performance, profit margins, shipping delays, and order cancellation drivers, alongside proactive prediction of late deliveries and shipping durations prior to dispatch. This project transforms raw transactional order-item records into a normalized SQL Server Snowflake Schema, an interactive four-page Power BI dashboard, and leakage-free machine learning pipelines.

## Project Objectives

- Analyze sales trends, profit margins, and cost distribution across regions, markets, and product categories.
- Evaluate shipping performance by comparing scheduled versus actual shipping days across shipping modes.
- Identify cancellation hotspots across payment methods, markets, and product categories.
- Design and populate a normalized **Snowflake Schema** data warehouse in SQL Server (`stg_dataco`, `fact_order_items`, and 15 dimension tables).
- Develop DAX measures and interactive KPIs in Microsoft Power BI.
- Build leakage-free Python machine learning pipelines for three targets: **Late Delivery Risk**, **Days for Shipping (Real)**, and **Benefit per Order**.
- Integrate out-of-sample test predictions (`36,104` rows), model comparisons, and feature importances directly into Power BI.

## Dataset

**DataCo Smart Supply Chain for Big Data Analysis (2015–2018)**

- **Original dataset:** `DataCoSupplyChainDataset.csv` (with `DescriptionDataCoSupplyChain.csv` data dictionary and `tokenized_access_logs.csv` clickstream logs).
- **Prepared dataset:** `DataCoSupplyChain_Cleaned.csv` — **180,519 rows × 34 columns**, with zero missing values.
- **Source:** [DataCo Smart Supply Chain for Big Data Analysis — Kaggle](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)

Both the original datasets and the cleaned dataset are stored in the `Data/` directory (`Data/Original data/` and `Data/Cleaned data/`).

## Tools and Technologies

- SQL Server & T-SQL (Snowflake Schema & `.bak` backup)
- Microsoft Power BI & DAX
- Python & Jupyter Notebook
- Pandas
- Scikit-learn (`StandardScaler`, `OneHotEncoder`, `SequentialFeatureSelector`, `LogisticRegression`, `LinearRegression`, `DecisionTreeClassifier`, `DecisionTreeRegressor`, `GridSearchCV`)
- Matplotlib

## Project Workflow

1. **Dataset preparation:** Clean and standardize the raw DataCo CSV into `DataCoSupplyChain_Cleaned.csv` (`180,519` order-item records × `34` columns, zero missing values).
2. **SQL database design:** Load staging data (`stg_dataco`), design a Snowflake Schema around `fact_order_items` and normalized customer, product, geography, date, and order/shipping dimensions, and export `CoSupplyChain.bak`.
3. **Power BI data preparation & measures:** Connect Power BI to the Snowflake Schema and develop DAX measures for sales, net sales, profit, cost, cancellation rate, shipping delays, and a moving ticker displaying live summary metrics.
4. **Predictive modeling & Power BI integration:** Implement three leakage-free 6-stage ML pipelines in Python (80/20 split, training-only preprocessing, forward feature selection, baseline linear vs. base & tuned Decision Trees), then link the `36,104` test-set predictions to `fact_order_items` via `Order Item Id` and build interactive Power BI modeling pages.
5. **Dashboard development:** Combine the analytical measures and predictive outputs into four interactive dashboard pages (**Overview**, **Sales & Profit**, **Shipping & Cancel Rate**, and **Predictive**).

**Workflow:** Original DataCo CSV → Data Cleaning (`DataCoSupplyChain_Cleaned.csv`, 34 columns) → SQL Server Snowflake Schema → Power BI Measures & Ticker → Python ML Pipelines & Power BI Predictive Integration → Interactive 4-Page Dashboard.

## Key Findings

The following figures are displayed across the Power BI analytical model and dashboard:

| Metric | Result |
|---|---:|
| Total Sales | 36.78M |
| Net Sales | 33.05M |
| Total Profit | 3.97M |
| Total Cost | 29.09M |
| Profit Margin % | 12% |
| Total Orders | 66K |
| Total Customers | 21K |
| Avg Order Value | 502.71 |
| Avg Scheduled Days | 2.93 |
| Avg Shipping Days | 3.50 |
| Avg Delay Days | 0.57 |
| Late Delivery % | 57.33% |
| Cancel Rate % | 0.02 (2%) |

These findings show that actual shipping averages **3.50 days** versus **2.93 scheduled days**, resulting in a **57.33%** late-delivery rate, with **First Class** and **Second Class** shipments experiencing the highest relative late-delivery percentages.

## Dashboard Features

The Power BI workbook (`Power BI/SupplyChain.pbix`) includes four main green-themed dashboard pages (`Power BI/dashboard/`):

### 1. Overview

[![Overview Dashboard](Power%20BI/dashboard/Overview.jpg)](Power%20BI/dashboard/Overview.jpg)
- **KPI Cards:** Total Sales (`36.78M`), Total Profit (`3.97M`), Profit Margin % (`12%`), Total Orders (`66K`), Total Customers (`21K`), Avg Order Value (`502.71`).
- **Charts:** Total Sales by month, Top 5 Products by Sales, Total Sales by market, and Total Sales by category.

### 2. Sales & Profit

[![Sales & Profit Dashboard](Power%20BI/dashboard/Sales_and_Profit.jpg)](Power%20BI/dashboard/Sales_and_Profit.jpg)
- **Charts:** Total Sales, Total Profit, and Total Cost by region; Top 10 categories by Total Profit; Top 10 categories by Total Sales; and Total Sales by customer segment (`Consumer` 51.91%, `Corporate` 30.36%, `Home Office` 17.73%).

### 3. Shipping & Cancel Rate

[![Shipping & Cancel Rate Dashboard](Power%20BI/dashboard/Shipping_and_Cancel_Rate.jpg)](Power%20BI/dashboard/Shipping_and_Cancel_Rate.jpg)
- **KPI Cards:** Avg Scheduled Days (`2.93`), Avg Shipping Days (`3.50`), Cancel Rate % (`0.02`), Late Delivery % (`57.33%`), Avg Delay Days (`0.57`).
- **Charts:** Late Delivery % by shipping mode, Top 10 categories by Cancel Rate %, Cancel Rate % by market, Avg Scheduled vs. Avg Shipping Days by shipping mode, and Total Orders by delivery status.

### 4. Predictive

[![Predictive Dashboard](Power%20BI/dashboard/Predictive.jpg)](Power%20BI/dashboard/Predictive.jpg)
- **KPI Cards:** Delivery Accuracy (`69.70%`), Delivery Precision, Days R² (`0.39`), Delivery F1 (`66.30%`), Days MAE (`0.98`), Test Sample (`36.104K`).
- **Charts:** Late Delivery Risk Feature Importance, Confusion Matrix (`Actual vs. Predicted`), Days For Shipping Feature Importance, and Actual vs. Predicted Avg. Shipping Days by Mode.

### Interactivity
- Dynamic slicers across pages filter metrics by `market_name`, `region_name`, `segment`, `category_name`, and `shipping_mode`.
- A moving ticker banner displays key analytical summary information across the dashboard.

## Predictive Modeling

Three supervised learning tasks were formulated on the `180,519` cleaned records (`144,415` train / `36,104` test) using an identical leakage-free 6-stage pipeline:

| Target Variable | Problem Type | Best / Tuned Model Metrics | Dominant Driver |
|---|---|---|---|
| **Late Delivery Risk** | Binary Classification | Accuracy: `69.7%`, Precision: `85.0%`, Recall: `54.4%`, F1: `66.3%` | `Days for shipment (scheduled)` (`99.79%`) |
| **Days for Shipping (Real)** | Regression | `R² = 0.392`, `MSE = 1.602`, `MAE = 0.981` days | `Days for shipment (scheduled)` (`99.84%`) |
| **Benefit per Order** | Regression | `R² = 0.024`, `MSE = 10,037.371`, `MAE = $54.068` | `Sales` (`79.65%`), `Category Name_COMPUTERS` (`10.67%`) |

Detailed scripts, CSV exports, Matplotlib plots, and Power BI snapshots for each target are organized under `Prediction models/`.

## Repository Structure

```text
supply-chain-dataset-analysis-final_project/
├── Data/
│   ├── Original data/
│   │   ├── DataCoSupplyChainDataset.csv
│   │   ├── DescriptionDataCoSupplyChain.csv
│   │   └── tokenized_access_logs.csv
│   ├── Cleaned data/
│   │   ├── Cleaning Data code.ipynb
│   │   └── DataCoSupplyChain_Cleaned.csv
│   └── README.md
├── Database/
│   ├── Database.zip
│   ├── Database_Schema.jpg
│   └── README.md
├── Power BI/
│   ├── SupplyChain.pbix
│   ├── Measures_KPIs.jpg
│   ├── Report_Visuals.jpg
│   ├── Modeling_Dashboard_Before.jpg
│   ├── dashboard/
│   │   ├── Overview.jpg
│   │   ├── Sales_and_Profit.jpg
│   │   ├── Shipping_and_Cancel_Rate.jpg
│   │   └── Predictive.jpg
│   └── README.md
├── Prediction models/
│   ├── Benefit per Order/
│   ├── Days for Shipping Real/
│   ├── Late Delivery Risk/
│   └── README.md
├── Report/
│   ├── Analysis and Measures.docx
│   ├── Predictive_Modeling_Report_Final.docx
│   └── README.md
└── README.md
```

## Reproduction

1. **Data:** Run `Data/Cleaned data/Cleaning Data code.ipynb` on `Data/Original data/DataCoSupplyChainDataset.csv` to reproduce `Data/Cleaned data/DataCoSupplyChain_Cleaned.csv`.
2. **SQL Server Database:** Extract `CoSupplyChain.bak` from `Database/Database.zip` and restore it in SQL Server Management Studio (SSMS) following `Database/Database_Schema.jpg`.
3. **Predictive Models:** Run the three Python scripts inside `Prediction models/<Target>/` (`late_delivery_risk_clean.py`, `days_for_shipping_real_clean.py`, `benefit_per_order_clean.py`) to reproduce the `*_predictions.csv`, `*_comparison.csv`, `*_importance.csv` outputs and plots.
4. **Power BI Dashboard:** Open `Power BI/SupplyChain.pbix` in Power BI Desktop, update data source paths if prompted, refresh the model, and explore all four dashboard pages.

## Data Quality and Preparation

Profiling and leakage-prevention steps applied before modeling:

- **Cleaned Dataset:** `180,519` order-item rows × `34` columns with zero missing values across `2015–2018`.
- **Excluded Identifiers:** `Category Id`, `Customer Id`, `Department Id`, `Order Id`, `Order Item Id` (retained only as Power BI join key), and `Product Card Id`.
- **Excluded High-Cardinality Columns:** `Customer City` (563 unique), `Order City` (3,597 unique), `Order State` (1,089 unique), `Order Country` (164 unique), and `Product Name` (118 unique).
- **Excluded Data-Leakage Columns:** `Delivery Status`, `DateOrders` (shipping date), `Order Status`, `Order Item Profit Ratio` (`r = 0.824` with profit), `Order Item Total`, and sibling target variables.

## Team Contributions

The project was completed collaboratively by **Team 5 (DEPI)**, with responsibilities divided across data cleaning, SQL Server warehousing, exploratory analysis, predictive modeling, and dashboard design:

- **Mohamed Salah:** SQL Server database design, Snowflake Schema modeling (`fact_order_items` and dimension tables), SQL scripts, and database backup (`Database/Database.zip`).
- **Donia Ragab and Dalia Hamdy:** Collaborated on data quality profiling, data cleaning (`Data/Cleaned data/Cleaning Data code.ipynb` & `DataCoSupplyChain_Cleaned.csv`), Exploratory Data Analysis (EDA), KPI definitions, DAX measures in Power BI (`Report/Analysis and Measures.docx`), and implementing the moving information ticker in the dashboard.
- **Omar El-Zayat:** Leakage-free predictive modeling in Python (`Scikit-learn`, `Pandas`, `Matplotlib`) across all three targets (`Late Delivery Risk`, `Days for Shipping Real`, `Benefit per Order`), Power BI predictive integration, and final modeling report (`Report/Predictive_Modeling_Report_Final.docx`).
- **Menna Emad:** Interactive Power BI dashboard design, KPI cards, charts, slicers, visual layout, and final dashboard exports (`Power BI/SupplyChain.pbix` & `Power BI/dashboard/`).

## References

- **Dataset:** [DataCo Smart Supply Chain for Big Data Analysis — Kaggle](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis) (2015–2018).
- **Documentation:** `Report/Analysis and Measures.docx` and `Report/Predictive_Modeling_Report_Final.docx`.
