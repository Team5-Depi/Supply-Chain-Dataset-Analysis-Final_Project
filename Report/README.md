# Report

This directory contains the unified final graduation project report for the Supply Chain Dataset Analysis project.

## Contents

- `Supply_Chain_Dataset_Analysis_Report.pdf`: Comprehensive 24-page technical and analytical report covering:
  - **Introduction & Project Goal**
  - **1. Project Planning:** 11 analytical questions, 3 predictive questions, scope & methodology, workflow, team roles, and risks & mitigation.
  - **2. Stakeholder Analysis:** Operational, financial, logistics, and data ownership stakeholders.
  - **3. Data and Database Design:** Data profiling (missing values, deduplication of 53 → 34 columns, 164 countries, 23 regions, 5 markets) and SQL Server Snowflake Schema (`stg_dataco`, `fact_order_items`, and 18 dimension tables).
  - **4. Exploratory Data Analysis & Key Findings:** Overall KPIs and all 11 business questions paired with their Power BI visuals and empirical answers.
  - **5. Predictive Modeling:** Leakage-free 6-stage pipelines (`StandardScaler`, `OneHotEncoder`, `Forward SequentialFeatureSelector (cv=3)`, `GridSearchCV`), confusion matrix, tuned decision trees, and actual vs. predicted plots across all three targets (`Late Delivery Risk`, `Days for Shipping Real`, `Benefit per Order`).
  - **6. UI/UX Design & Web Application:** Four green-themed Power BI dashboard pages (`Overview`, `Sales & Profit`, `Shipping & Cancel Rate`, `Predictive`), user flow, design principles, and the standalone bilingual HTML web application (`Website/Website.html`).
  - **7. Conclusion & 8. Business Recommendations:** Early warning alerts (~85% Precision), SLA recalibration, future COGS/carrier data enrichment, and key variables to monitor.
