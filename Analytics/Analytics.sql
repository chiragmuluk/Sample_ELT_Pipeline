-- Databricks notebook source
-- MAGIC %md 
-- MAGIC **Query 1**
-- MAGIC
-- MAGIC Top 5 products by total sales revenue

-- COMMAND ----------

WITH completedOrders AS (
    SELECT
        product_hash_key,
        total_amount,
        ROW_NUMBER() OVER (ORDER BY total_amount DESC) AS rk
    FROM
        workspace.insulet_uk_curated.fact_sales_transactions
),
top_products AS (
    SELECT
        *
    FROM
        completedOrders
    WHERE
        rk < 6
)

SELECT
    product_name,
    total_amount
FROM
    top_products
    INNER JOIN workspace.insulet_uk_curated.dim_products USING (product_hash_key)

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC **Query 2**
-- MAGIC
-- MAGIC Monthly revenue trend for the past 12 months

-- COMMAND ----------

SELECT
    calendar_year AS revenue_year,
    calendar_month AS revenue_month,
    ROUND(SUM(total_amount), 2) AS monthly_revenue
FROM
    workspace.insulet_uk_curated.fact_sales_transactions
    INNER JOIN workspace.insulet_uk_curated.dim_calendar
        USING (calendar_hash_key)
WHERE
    full_date >= date_add(MONTH, -12, current_date())
GROUP BY
    revenue_year,
    revenue_month

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC **Query 3**
-- MAGIC
-- MAGIC Customer lifetime value (total revenue per customer)

-- COMMAND ----------

SELECT
    customer_id AS customer_id,
    CONCAT_WS(' ', first_name, last_name) AS customer_name,
    ROUND(SUM(total_amount), 2) AS total_sales
FROM
    workspace.insulet_uk_curated.fact_sales_transactions AS completedorders
    LEFT JOIN workspace.insulet_uk_curated.dim_customers USING (customer_hash_key)
GROUP BY
    completedorders.customer_hash_key,
    customer_id,
    CONCAT_WS(' ', first_name, last_name)
