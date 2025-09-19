# Databricks notebook source
# MAGIC %md
# MAGIC # UK Sales Analytics
# MAGIC
# MAGIC This project analyzes sales transactions for UK using Databricks and AWS. It leverages curated fact and dimension tables to provide insights into product performance, customer sales, and revenue trends.
# MAGIC
# MAGIC ## Data Sources 
# MAGIC
# MAGIC - **Raw Data:** CSV files stored in Databricks workspace volumes at  
# MAGIC - **Fact Table:** `workspace.insulet_uk_curated.fact_sales_transactions`
# MAGIC   - Contains sales transactions with order, customer, product, and calendar hash keys, quantities, and total amounts.
# MAGIC - **Dimension Tables:**
# MAGIC   - `workspace.insulet_uk_curated.dim_products`: Product details.
# MAGIC   - `workspace.insulet_uk_curated.dim_customers`: Customer details.
# MAGIC   - `workspace.insulet_uk_curated.dim_calendar`: Calendar dates.
# MAGIC
# MAGIC ## Key Notebooks & Queries
# MAGIC
# MAGIC - **Top Products by Revenue**
# MAGIC   - Identifies the top 5 products by total sales amount.
# MAGIC - **Monthly Revenue Trends**
# MAGIC   - Aggregates revenue by year and month for the last 12 months.
# MAGIC - **Customer Sales Summary**
# MAGIC   - Summarizes total sales per customer.
# MAGIC
# MAGIC ## Usage
# MAGIC
# MAGIC 1. Open the Databricks notebook in your AWS workspace.
# MAGIC 2. Run the provided SQL cells to generate insights.
# MAGIC 3. Visualize results using Databricks display features.
# MAGIC
# MAGIC ## AWS Integration
# MAGIC
# MAGIC All data is stored and processed in AWS, ensuring scalability and security.
# MAGIC
# MAGIC ## Project Structure
# MAGIC
# MAGIC - Notebooks: SQL queries for analysis.
# MAGIC - Data: Curated fact and dimension tables in the `workspace.insulet_uk_curated` schema.
# MAGIC - Raw Data: CSV files in Databricks workspace volumes.
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Future Scope
# MAGIC
# MAGIC 1. **Incorporating Auto Loader**
# MAGIC    - Integrate Databricks Auto Loader to automate ingestion of new data files and enable schema evolution for flexible, scalable data pipelines.
# MAGIC
# MAGIC 2. **Centralized System to Store Data Quality Rules**
# MAGIC    - Develop a centralized repository (e.g., Delta table or Python module) to manage and version data quality rules, enabling dynamic rule application and governance.
# MAGIC
# MAGIC 3. **Implementing Unit Test Cases**
# MAGIC    - Establish a suite of unit tests for data processing scripts and data quality logic to ensure reliability and catch regressions early.
# MAGIC
# MAGIC 4. **Implementing AES Encryption on Sensitive Data**
# MAGIC    - Apply AES encryption to sensitive columns during ingestion or prior to storage, ensuring compliance with data security standards.
# MAGIC
# MAGIC 5. **Implementing User-Level Access**
# MAGIC    - Enforce user-level access controls using Databricks' built-in access management or table ACLs to restrict data visibility and operations based on user roles.
# MAGIC
# MAGIC 6. **Expanding Raw Data Processing Script for Date Range Loading**
# MAGIC    - Enhance data loading scripts to support filtering and loading data within a specified date range (if Auto Loader is not implemented).
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ![](Data Model.png)
