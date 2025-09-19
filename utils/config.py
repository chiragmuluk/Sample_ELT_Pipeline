# Databricks notebook source
base_path='/Volumes/workspace/insulet'

# COMMAND ----------

raw_products='{}/raw/products'.format(base_path)
raw_orders='{}/raw/orders'.format(base_path)
raw_customers='{}/raw/customers'.format(base_path)


# COMMAND ----------

raw_uk_schema='insulet_uk_raw'
raw_customers_table='customers'
raw_orders_table='orders'
raw_products_table='products'

# COMMAND ----------

enriched_uk_schema='insulet_uk_enriched'
cleaned_customers_table='cleaned_customers'
cleaned_orders_table='cleaned_orders'
cleaned_products_table='cleaned_products'

# COMMAND ----------

curated_uk_schema='insulet_uk_curated'
dim_customers_table='dim_customers'
dim_calendar_table='dim_calendar'
dim_products_table='dim_products'
fact_sales_transactions_table='fact_sales_transactions'


# COMMAND ----------

data_quality_uk_schema = 'insulet_uk_quarantine'
data_quality_customer_table = 'customers'
data_quality_order_table = 'orders'
data_quality_product_table = 'products'
