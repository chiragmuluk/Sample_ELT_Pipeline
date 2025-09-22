# UK Sales Analytics

This project analyzes sales transactions for the UK using Databricks and AWS. It leverages curated fact and dimension tables to provide insights into product performance, customer sales, and revenue trends.

## Data Sources

- **Raw Data:** CSV files stored in Databricks workspace volumes.
- **Fact Table:** `workspace.insulet_uk_curated.fact_sales_transactions`
  - Contains sales transactions with order, customer, product, and calendar hash keys, quantities, and total amounts.
- **Dimension Tables:**
  - `workspace.insulet_uk_curated.dim_products`: Product details.
  - `workspace.insulet_uk_curated.dim_customers`: Customer details.
  - `workspace.insulet_uk_curated.dim_calendar`: Calendar dates.

## Key Notebooks & Queries

- **Top Products by Revenue**
  - Identifies the top 5 products by total sales amount.
- **Monthly Revenue Trends**
  - Aggregates revenue by year and month for the last 12 months.
- **Customer Sales Summary**
  - Summarizes total sales per customer.

## Usage

1. Open the Databricks notebook in your AWS workspace.
2. Run the provided SQL cells to generate insights.
3. Visualize results using Databricks display features.

## AWS Integration

All data is stored and processed in AWS, ensuring scalability and security.

## Project Structure

- **Notebooks:** SQL queries for analysis.
- **Data:** Curated fact and dimension tables in the `workspace.insulet_uk_curated` schema.
- **Raw Data:** CSV files in Databricks workspace volumes.

## Future Scope

1. **Incorporating Auto Loader**
   - Integrate Databricks Auto Loader to automate ingestion of new data files and enable schema evolution for flexible, scalable data pipelines.
2. **Centralized System to Store Data Quality Rules**
   - Develop a centralized repository (e.g., Delta table or Python module) to manage and version data quality rules, enabling dynamic rule application and governance.
3. **Implementing Unit Test Cases**
   - Establish a suite of unit tests for data processing scripts and data quality logic to ensure reliability and catch regressions early.
4. **Implementing AES Encryption on Sensitive Data**
   - Apply AES encryption to sensitive columns during ingestion or prior to storage, ensuring compliance with data security standards.
5. **Implementing User-Level Access**
   - Enforce user-level access controls using Databricks' built-in access management or table ACLs to restrict data visibility and operations based on user roles.
6. **Expanding Raw Data Processing Script for Date Range Loading**
   - Enhance data loading scripts to support filtering and loading data within a specified date range (if Auto Loader is not implemented).
7. **Implementing CI/CD for Automated Deployment**
   - Set up CI/CD pipelines (e.g., using Databricks Asset Bundles, GitHub Actions, or Jenkins) to automate validation, testing, and deployment of code and notebooks across multiple environments (dev, test, prod), reducing manual intervention and ensuring consistent releases.

> **Note:** The current code and analysis are developed specifically for the UK region.

## Data Model

![Data Model](Data%20Model.png)