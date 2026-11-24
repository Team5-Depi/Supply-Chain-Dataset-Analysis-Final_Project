# Data

This directory stores both the original raw DataCo Supply Chain files and the cleaned dataset used across the SQL Server data warehouse, Power BI model, and Python machine learning pipelines.

## Directory Structure

```text
Data/
├── Original data/
│   ├── DataCoSupplyChainDataset.csv
│   ├── DescriptionDataCoSupplyChain.csv
│   └── tokenized_access_logs.csv
└── Cleaned data/
    └── DataCoSupplyChain_Cleaned.csv
```

## Dataset Details

- **Original data (`Original data/`):**
  - `DataCoSupplyChainDataset.csv`: Raw transactional supply chain dataset.
  - `DescriptionDataCoSupplyChain.csv`: Field-level data dictionary describing original columns.
  - `tokenized_access_logs.csv`: Raw web clickstream/access logs.
- **Cleaned data (`Cleaned data/`):**
  - `DataCoSupplyChain_Cleaned.csv`: Standardized dataset containing **180,519 order-item records × 34 columns**, covering **2015–2018** with **zero missing values**.
