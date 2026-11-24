# Interactive Supply Chain Web Application (`Website.html`)

A standalone, responsive HTML5/CSS3/JavaScript web application that mirrors the Power BI dashboard and supports full client-side CSV loading (up to **180,519 rows** from `DataCoSupplyChain_Cleaned.csv`).

## Features

- **Built-in 55-Row Preview Sample:** Opens immediately with a 55-row sample across all regions, markets, categories, and shipping modes.
- **Full CSV Upload (`PapaParse`):** Click **📂 Upload CSV** to load `Data/Cleaned data/DataCoSupplyChain_Cleaned.csv` (180,519 rows) directly in the browser with single-pass aggregation.
- **6 Interactive Pages:**
  1. **Overview:** 6 KPI cards and 4 interactive charts (monthly sales trend, top 5 products, sales by market, sales by category).
  2. **Sales & Profit:** Regional Sales/Profit/Cost comparison, top 10 categories by profit and sales, and sales by customer segment.
  3. **Shipping & Cancel Rate:** 5 shipping KPIs, late delivery % by mode, top 10 cancel rate categories, cancel rate by market, scheduled vs. real shipping days, and delivery status distribution.
  4. **Predictive:** Model evaluation KPIs (`69.70%` Accuracy, `84.92%` Precision, `0.39` Days R², `66.30%` F1, `0.98` Days MAE), confusion matrix (`36,104` test sample), feature importances, and actual vs. predicted shipping days.
  5. **Data Records:** Paginated order table (15 rows per page) synced with active filters.
  6. **+ Add Order:** Form to add new supply chain orders (`localStorage` persistence) and update all KPIs and charts immediately.
- **Interactive Filtering & Bilingual Support:** Top slicers (`market_name`, `category_name`, `shipping_mode`, `segment`), chart-click cross-filtering, and **Arabic / English** toggle with RTL/LTR layout switching.

## How to Run

1. Open `Website/Website.html` in any modern web browser.
2. Explore the built-in 55-row sample or click **📂 Upload CSV** and select `Data/Cleaned data/DataCoSupplyChain_Cleaned.csv` to analyze the full dataset.
