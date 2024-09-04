from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Product Sales Analysis") \
    .getOrCreate()

# Sample data for products
products = [
    (1, "Laptop", "Electronics", 50000),
    (2, "Smartphone", "Electronics", 30000),
    (3, "Table", "Furniture", 15000),
    (4, "Chair", "Furniture", 5000),
    (5, "Headphones", "Electronics", 2000),
]

# Sample data for sales transactions
sales = [
    (1, 1, 2),
    (2, 2, 1),
    (3, 3, 3),
    (4, 1, 1),
    (5, 4, 5),
    (6, 2, 2),
    (7, 5, 10),
    (8, 3, 1),]


# Define schema for DataFrames
product_columns = ["ProductID", "ProductName", "Category", "Price"]
sales_columns = ["SaleID", "ProductID", "Quantity"]

# Create DataFrames
product_df = spark.createDataFrame(products, schema=product_columns)
sales_df = spark.createDataFrame(sales, schema=sales_columns)

# Show the DataFrames
print("Products DataFrame:")
product_df.show()

print("Sales DataFrame:")
sales_df.show()

# 1. **Join the DataFrames:** 
#    - Join the `product_df` and `sales_df` DataFrames on `ProductID` to create a combined DataFrame with product and sales data.
combined_df = sales_df.join(product_df, on="ProductID", how="inner")
print("Combined DataFrame (Products + Sales):")
combined_df.show()

# 2. **Calculate Total Sales Value:**
#    - For each product, calculate the total sales value by multiplying the price by the quantity sold.
combined_df = combined_df.withColumn("TotalSalesValue", col("Price") * col("Quantity"))
print("DataFrame with Total Sales Value:")
combined_df.show()

# 3. **Find the Total Sales for Each Product Category:**
#    - Group the data by the `Category` column and calculate the total sales value for each product category.
category_sales_df = combined_df.groupBy("Category").sum("TotalSalesValue").withColumnRenamed("sum(TotalSalesValue)","TotalCategorySales")
print("Total Sales for Each Product Category:")
category_sales_df.show()

# 4. **Identify the Top-Selling Product:**
#    - Find the product that generated the highest total sales value.
top_selling_product_df = combined_df.groupBy("ProductID", "ProductName").sum("TotalSalesValue").withColumnRenamed("sum(TotalSalesValue)","TotalSalesValue")
top_selling_product_df = top_selling_product_df.orderBy(col("TotalSalesValue").desc())
print("Top-Selling Product:")
top_selling_product_df.show(1)

# 5. **Sort the Products by Total Sales Value:**
#    - Sort the products by total sales value in descending order.
sorted_products_df = top_selling_product_df.orderBy(col("TotalSalesValue").desc())
print("Products Sorted by Total Sales Value:")
sorted_products_df.show()
                            
# 6. **Count the Number of Sales for Each Product:**
#    - Count the number of sales transactions for each product.
sales_count_df = combined_df.groupBy("ProductID", "ProductName").count().withColumnRenamed("count()","NumberOfSales")
print("Number of Sales for Each Product:")
sales_count_df.show()                           
                            
# 7. **Filter the Products with Total Sales Value Greater Than ₹50,000:**
#    - Filter out the products that have a total sales value greater than ₹50,000.
high_sales_df = top_selling_product_df.filter(col("TotalSalesValue") > 50000)
print("Products with Total Sales Value Greater Than ₹50,000:")
high_sales_df.show()

