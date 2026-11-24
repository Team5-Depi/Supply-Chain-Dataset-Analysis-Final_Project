# Database

This directory contains the SQL Server data warehouse backup and entity-relationship diagram for the Supply Chain project.

## Contents

- `Database.zip`: Compressed archive containing `CoSupplyChain.bak` (compressed to stay within GitHub's 100 MB file size limit).
- `Database_Schema.jpg`: Snowflake Schema diagram illustrating the staging table (`stg_dataco`), the central fact table (`fact_order_items`), and normalized dimension tables (`dim_customer`, `dim_customer_segment`, `dim_customer_city`, `dim_customer_state`, `dim_customer_country`, `dim_product`, `dim_category`, `dim_department`, `dim_order_city`, `dim_order_state`, `dim_order_country`, `dim_region`, `dim_market`, `dim_shipping_mode`, `dim_payment_type`, `dim_delivery_status`, `dim_order_status`, and `dim_date`).

## Restoration Steps

1. Extract `CoSupplyChain.bak` from `Database.zip`.
2. Open SQL Server Management Studio (SSMS), right-click **Databases** > **Restore Database...**, choose **Device**, and select `CoSupplyChain.bak`.
