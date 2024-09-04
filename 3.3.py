from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Key-Value Pair RDDs Exercise") \
    .getOrCreate()

# Get the SparkContext from SparkSession
sc = spark.sparkContext

#Task 1: Create an RDD from the Sales Data
sales_data = [
    ("ProductA", 100),
    ("ProductB", 150),
    ("ProductA", 200),
    ("ProductC", 300),
    ("ProductB", 250),
    ("ProductC", 100)
]

# Create an RDD from sales_data
sales_rdd = sc.parallelize(sales_data)

# Print the first few elements of the RDD
print("Sales RDD:")
print(sales_rdd.take(5))

#Task 2: Group Data by Product Name
# Group the sales data by product name
grouped_rdd = sales_rdd.groupByKey()

# Print the grouped data
print("Grouped Data:")
for product, sales in grouped_rdd.collect():
    print(product, list(sales))


#Task 3: Calculate Total Sales by Product 
# Calculate total sales for each product using reduceByKey
total_sales_rdd = sales_rdd.reduceByKey(lambda x, y: x + y)

# Print the total sales for each product
print("Total Sales by Product:")
total_sales_rdd.collect()


#Task 4: Sort Products by Total Sales
# Sort the products by total sales in descending order
sorted_sales_rdd = total_sales_rdd.sortBy(lambda x: x[1], ascending=False)

# Print the sorted list of products
print("Sorted Products by Total Sales:")
sorted_sales_rdd.collect()


#Task 5: Filter Products with High Sales
# Filter products with total sales greater than 200
high_sales_rdd = total_sales_rdd.filter(lambda x: x[1] > 200)

# Print the products that meet this condition
print("Products with Sales Greater Than 200:")
high_sales_rdd.collect()


#Task 6: Combine Regional Sales Data

# Regional sales data
regional_sales_data = [
    ("ProductA", 50),
    ("ProductC", 150)
]

# Create an RDD from regional_sales_data
regional_sales_rdd = sc.parallelize(regional_sales_data)

# Combine the sales RDDs using union
combined_rdd = sales_rdd.union(regional_sales_rdd)

# Calculate the new total sales for each product after combining the datasets
combined_total_sales_rdd = combined_rdd.reduceByKey(lambda x, y: x + y)

# Print the combined sales data
print("Combined Sales Data:")
combined_total_sales_rdd.collect()

#Task 7: Count the Number of Distinct Products

# Count the number of distinct products
distinct_products_count = combined_total_sales_rdd.keys().distinct().count()

# Print the count of distinct products
print("Number of Distinct Products:", distinct_products_count)


#Task 8: Identify the Product with Maximum Sales
# Find the product with the maximum total sales using reduce
max_sales_product = combined_total_sales_rdd.reduce(lambda x, y: x if x[1] > y[1] else y)

# Print the product name and its total sales amount
print("Product with Maximum Sales:", max_sales_product)

#Challenge Task

# Calculate the total quantity sold for each product
total_quantity_rdd = sales_rdd.mapValues(lambda x: 1).reduceByKey(lambda x, y: x + y)

# Join total sales and total quantity RDDs
total_sales_quantity_rdd = total_sales_rdd.join(total_quantity_rdd)

# Calculate the average sales amount per product
avg_sales_rdd = total_sales_quantity_rdd.mapValues(lambda x: x[0] / x[1])

# Print the average sales for each product
print("Average Sales per Product:")
avg_sales_rdd.collect()
