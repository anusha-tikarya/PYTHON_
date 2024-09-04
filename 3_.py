# *Step 1: Generate the Sample Sales Dataset*
import pandas as pd
from datetime import datetime
# Sample sales data
data = {
    "TransactionID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "CustomerID": [101, 102, 103, 101, 104, 102, 103, 104, 101, 105],
    "ProductID": [501, 502, 501, 503, 504, 502, 503, 504, 501, 505],
    "Quantity": [2, 1, 4, 3, 1, 2, 5, 1, 2, 1],
    "Price": [150.0, 250.0, 150.0, 300.0, 450.0, 250.0, 300.0, 450.0, 150.0, 550.0],
    "Date": [
        datetime(2024, 9, 1),
        datetime(2024, 9, 1),
        datetime(2024, 9, 2),
        datetime(2024, 9, 2),
        datetime(2024, 9, 3),
        datetime(2024, 9, 3),
        datetime(2024, 9, 4),
        datetime(2024, 9, 4),
        datetime(2024, 9, 5),
        datetime(2024, 9, 5)
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)
# Save the DataFrame to a CSV file
df.to_csv('sales_data.csv', index=False)
print("Sample sales dataset has been created and saved as 'sales_data.csv'.")
from pyspark.sql import SparkSession
# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Sales Dataset Analysis") \
    .getOrCreate()
 # Load the sales dataset
sales_df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)
# Show the first few rows of the DataFrame
sales_df.show()
# Display the schema of the DataFrame
sales_df.printSchema()
# Display the first 5 rows of the DataFrame
sales_df.show(5)
# Get summary statistics for numeric columns (Quantity and Price)
sales_df.describe(["Quantity", "Price"]).show()
from pyspark.sql.functions import col
# Add a new column for TotalSales (Quantity * Price)
sales_df = sales_df.withColumn("TotalSales", col("Quantity") * col("Price"))
# Show the updated DataFrame
sales_df.show()
# Group by ProductID and calculate total sales for each product
product_sales_df = sales_df.groupBy("ProductID").sum("TotalSales").withColumnRenamed("sum(TotalSales)","TotalProductSales")
# Show the result
product_sales_df.show()
# Find the product with the highest total sales
top_selling_product_df = product_sales_df.orderBy(col("TotalProductSales").desc())
# Show the top-selling product
top_selling_product_df.show(1)
# Group by Date and calculate total sales for each day
daily_sales_df = sales_df.groupBy("Date").sum("TotalSales").withColumnRenamed("sum(TotalSales)","TotalDailySales")
# Show the result
daily_sales_df.show()
# Filter transactions with TotalSales greater than ₹500
high_value_sales_df = sales_df.filter(col("TotalSales") > 500)
# Show the filtered transactions
high_value_sales_df.show()
# Count the number of purchases made by each customer
repeat_customers_df = sales_df.groupBy("CustomerID").count().filter(col("count") > 1)
# Show repeat customers
repeat_customers_df.show()
# Calculate the average price per product
avg_price_per_product_df = sales_df.groupBy("ProductID").agg(sum("TotalSales") / sum("Quantity"))
# Show the average price per product
avg_price_per_product_df.show()
