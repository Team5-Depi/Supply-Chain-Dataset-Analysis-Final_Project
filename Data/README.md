# Data

This directory stores both the original raw DataCo Supply Chain files and the cleaned dataset + preprocessing notebook used across the SQL Server data warehouse, Power BI model, and Python machine learning pipelines.

## Directory Structure

```text
Data/
├── Original data/
│   ├── DataCoSupplyChainDataset.csv
│   ├── DescriptionDataCoSupplyChain.csv
│   └── tokenized_access_logs.csv
└── Cleaned data/
    ├── Cleaning Data code.ipynb
    └── DataCoSupplyChain_Cleaned.csv
```

## Dataset & Cleaning Details

- **Source:** [DataCo Smart Supply Chain for Big Data Analysis — Kaggle](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)

- **Original data (`Original data/`):**
  - `DataCoSupplyChainDataset.csv`: Raw transactional supply chain dataset (53 columns).
  - `DescriptionDataCoSupplyChain.csv`: Field-level data dictionary describing original columns.
  - `tokenized_access_logs.csv`: Raw web clickstream/access logs.
- **Cleaned data (`Cleaned data/`):**
  - `Cleaning Data code.ipynb`: Python/Jupyter preprocessing notebook (`pandas`, `numpy`, `matplotlib`, `seaborn`) that inspects missing values and duplicates, drops unnecessary/sensitive/redundant columns (`Customer Email`, `Customer Password`, `Customer Fname`, `Customer Lname`, `Customer Street`, `Product Description`, `Product Image`, `Product Status`, `Order Zipcode`, etc.), standardizes text casing and whitespace, parses `order date (DateOrders)` and `shipping date (DateOrders)` to `datetime`, profiles outliers via IQR and boxplots, and exports the cleaned CSV.
  - `DataCoSupplyChain_Cleaned.csv`: Standardized dataset containing **180,519 order-item records**, covering **2015–2018** with **zero missing values**.
