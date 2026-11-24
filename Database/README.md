# Database (SQL Server Data Warehouse)

This folder contains the SQL Server database backup and entity-relationship diagram for the Supply Chain Data Warehouse.

## Contents

- `Database.zip`: Compressed SQL Server backup archive containing `CoSupplyChain.bak` (compressed to meet GitHub's 100 MB file size limit).
- `Database_Schema.jpg`: Full Snowflake Schema diagram showing staging (`stg_dataco`), the central fact table (`fact_order_items`), and normalized dimension tables (`dim_customer`, `dim_product`, `dim_category`, `dim_department`, `dim_order_city`, `dim_order_state`, `dim_order_country`, `dim_region`, `dim_market`, `dim_shipping_mode`, `dim_payment_type`, `dim_delivery_status`, `dim_order_status`, `dim_date`, etc.).

## How to Restore

1. Extract `CoSupplyChain.bak` from `Database.zip`.
2. In SQL Server Management Studio (SSMS), right-click **Databases** > **Restore Database...** > select **Device** and point to `CoSupplyChain.bak`.
