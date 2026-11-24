# Data

This folder contains both the original raw files and the cleaned dataset used across SQL Server, Power BI, and the Machine Learning pipelines.

## Contents

### 1. `Original data/`
- `DataCoSupplyChainDataset.csv`: Raw DataCo Supply Chain dataset (~180,519 rows).
- `DescriptionDataCoSupplyChain.csv`: Data dictionary describing each field in the original dataset.
- `tokenized_access_logs.csv`: Raw web clickstream/access logs associated with the DataCo store.

### 2. `Cleaned data/`
- `DataCoSupplyChain_Cleaned.csv`: Cleaned and standardized dataset (**180,519 order-item records**, **34 columns**, **zero missing values**, covering **2015–2018**).
