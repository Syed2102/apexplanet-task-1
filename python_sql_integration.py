# ApexPlanet Internship - Task 2
# Step 2: Import required libraries

import os
import sqlite3
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from pathlib import Path

# Print a message to check Python setup
# print("Python and SQL libraries are ready!")
# ApexPlanet Internship - Task 2
# Step 3: Connect Python to SQLite database

from sqlalchemy import create_engine

# Create a connection to SQLite database
engine = create_engine("sqlite:///superstore.db")

# Check database connection
with engine.connect() as connection:
    print("Database connected successfully!")
# Display all files in the current folder

# import os

# print(os.listdir())
# ApexPlanet Internship - Task 2
# Check files inside the data folder

# import os

# Display all files inside data folder
# print(os.listdir("data"))
# ApexPlanet Internship - Task 2
# Step 6: Import Superstore dataset into SQLite

# import pandas as pd

# Read CSV file from the data folder
# df = pd.read_csv("data/sample-superstore-cleaned.csv")

# Save dataset into SQLite database
# df.to_sql(
#     "superstore",
#     engine,
#     if_exists="replace",
#     index=False
# )

# Display success message
# print("Superstore dataset imported successfully!")

# Display first 5 rows
# print(df.head())

# Display total number of rows and columns
# print("Dataset Shape:", df.shape)
# ApexPlanet Internship - Task 2
# Step 7: Read SQL data using pandas

# import pandas as pd

# SQL query to retrieve first 10 rows
# query = """
# SELECT *
# FROM superstore
# LIMIT 10;
# """

# Read SQL query result into pandas DataFrame
# data = pd.read_sql(query, engine)

# Display the result
# print(data)

# Display dataset information
# print("Total Rows:", len(data))
# ApexPlanet Internship - Task 2
# Step 8: Calculate total sales and profit

# import pandas as pd

# SQL query to calculate total sales and profit
# query = """
# SELECT
#     SUM(Sales) AS total_sales,
#     SUM(Profit) AS total_profit
# FROM superstore;
# """

# Execute query using pandas
# data = pd.read_sql(query, engine)

# Display result
# print("Total Sales and Profit:")
# print(data)
# ApexPlanet Internship - Task 2
# Step 9: Sales Analysis by Category

# import pandas as pd

# SQL query to calculate category-wise sales
# query = """
# SELECT
#     Category,
#     SUM(Sales) AS total_sales
# FROM superstore
# GROUP BY Category
# ORDER BY total_sales DESC;
# """

# Execute SQL query using pandas
# data = pd.read_sql(query, engine)

# Display category-wise sales
# print("Category-wise Sales:")
# print(data)
# ApexPlanet Internship - Task 2

# Check column names in the Superstore dataset

# import pandas as pd

# # Read the dataset
# df = pd.read_csv("data/sample-superstore-cleaned.csv")

# # Display all column names
# print(df.columns.tolist())
# ApexPlanet Internship - Task 2
# Step 10: Customer-wise Sales Analysis

# import pandas as pd

# # SQL query to find top 10 customers
# query = """
# SELECT
#     "Customer Name",
#     SUM(Sales) AS total_sales
# FROM superstore
# GROUP BY "Customer Name"
# ORDER BY total_sales DESC
# LIMIT 10;
# """

# # Execute SQL query using pandas
# data = pd.read_sql(query, engine)

# # Display top customers
# print("Top 10 Customers by Sales:")
# print(data)
# Step 11: Calculate total sales and total profit

# query = """
# SELECT
#     SUM(Sales) AS total_sales,
#     SUM(Profit) AS total_profit
# FROM superstore;
# """

# # Execute SQL query using pandas
# data = pd.read_sql(query, engine)

# # Display the result
# print("\nTotal Sales and Total Profit:")
# print(data)
# Step 12: Sales analysis by category

# query = """
# SELECT
#     Category,
#     SUM(Sales) AS total_sales,
#     SUM(Profit) AS total_profit
# FROM superstore
# GROUP BY Category
# ORDER BY total_sales DESC;
# """

# # Execute SQL query using pandas
# data = pd.read_sql(query, engine)

# # Display category-wise sales and profit
# print("\nSales Analysis by Category:")
# print(data)
# Step 13: Monthly sales analysis

# query = """
# SELECT
#     strftime('%Y-%m', "Order Date") AS month,
#     SUM(Sales) AS monthly_sales
# FROM superstore
# GROUP BY month
# ORDER BY month;
# """

# # Execute SQL query using pandas
# data = pd.read_sql(query, engine)

# # Display monthly sales
# print("\nMonthly Sales Analysis:")
# print(data)
# Step 14: Regional sales analysis

# query = """
# SELECT
#     Region,
#     SUM(Sales) AS total_sales,
#     SUM(Profit) AS total_profit
# FROM superstore
# GROUP BY Region
# ORDER BY total_sales DESC;
# """

# # Execute SQL query using pandas
# data = pd.read_sql(query, engine)

# # Display regional sales
# print("\nRegional Sales Analysis:")
# print(data)
# Step 15: Top 10 products by sales

# query = """
# SELECT
#     "Product Name",
#     SUM(Sales) AS total_sales
# FROM superstore
# GROUP BY "Product Name"
# ORDER BY total_sales DESC
# LIMIT 10;
# """

# # Execute SQL query using pandas
# data = pd.read_sql(query, engine)

# # Display top 10 products
# print("\nTop 10 Products by Sales:")
# print(data)
# Import matplotlib for visualization
# import matplotlib.pyplot as plt
# # Step 16: Visualize sales by category

# query = """
# SELECT
#     Category,
#     SUM(Sales) AS total_sales
# FROM superstore
# GROUP BY Category
# ORDER BY total_sales DESC;
# """

# # Fetch SQL data into pandas DataFrame
# data = pd.read_sql(query, engine)

# # Create bar chart
# plt.figure(figsize=(8, 5))
# plt.bar(data["Category"], data["total_sales"])

# # Add chart title and labels
# plt.title("Total Sales by Product Category")
# plt.xlabel("Product Category")
# plt.ylabel("Total Sales")

# # Display chart
# plt.tight_layout()
# plt.show()
# Import Path to manage folders
# from pathlib import Path
# # Step 17: Save chart as PNG

# # Create visualizations folder if it does not exist
# Path("visualizations").mkdir(exist_ok=True)

# # Adjust chart layout
# plt.tight_layout()

# # Save chart
# plt.savefig("visualizations/sales_by_category.png", dpi=300)

# # Display chart
# plt.show()

# print("Chart saved successfully!")
# Step 18: Top 10 Customers by Sales Visualization

# query = """
# SELECT
#     "Customer Name",
#     SUM(Sales) AS total_sales
# FROM superstore
# GROUP BY "Customer Name"
# ORDER BY total_sales DESC
# LIMIT 10;
# """

# # Fetch data from SQL
# data = pd.read_sql(query, engine)

# # Create bar chart
# plt.figure(figsize=(10, 6))
# plt.barh(data["Customer Name"], data["total_sales"])

# # Reverse order so highest sales is at the top
# plt.gca().invert_yaxis()

# # Add title and labels
# plt.title("Top 10 Customers by Sales")
# plt.xlabel("Total Sales")
# plt.ylabel("Customer Name")

# # Save chart
# plt.tight_layout()
# plt.savefig("visualizations/top_10_customers.png", dpi=300)

# # Display chart
# plt.show()

# print("Top 10 Customers chart saved successfully!")
# Step 19: Monthly Sales Trend Visualization

# query = """
# SELECT
#     strftime('%Y-%m', "Order Date") AS month,
#     SUM(Sales) AS monthly_sales
# FROM superstore
# GROUP BY month
# ORDER BY month;
# """

# # Fetch data from SQL
# data = pd.read_sql(query, engine)

# # Create line chart
# plt.figure(figsize=(12, 6))
# plt.plot(data["month"], data["monthly_sales"], marker="o")

# # Add title and labels
# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Monthly Sales")

# # Rotate month labels
# plt.xticks(rotation=45)

# # Adjust layout
# plt.tight_layout()

# # Save chart
# plt.savefig("visualizations/monthly_sales_trend.png", dpi=300)

# # Display chart
# plt.show()

# print("Monthly Sales Trend chart saved successfully!")
# Step 20: Regional Sales Visualization

# query = """
# SELECT
#     Region,
#     SUM(Sales) AS total_sales
# FROM superstore
# GROUP BY Region
# ORDER BY total_sales DESC;
# """

# # Fetch data from SQL
# data = pd.read_sql(query, engine)

# # Create bar chart
# plt.figure(figsize=(8, 5))
# plt.bar(data["Region"], data["total_sales"])

# # Add title and labels
# plt.title("Total Sales by Region")
# plt.xlabel("Region")
# plt.ylabel("Total Sales")

# # Adjust layout
# plt.tight_layout()

# # Save chart
# plt.savefig("visualizations/regional_sales.png", dpi=300)

# # Display chart
# plt.show()

# print("Regional Sales chart saved successfully!")
# Step 21: Sales vs Profit Visualization

# query = """
# SELECT
#     Sales,
#     Profit
# FROM superstore;
# """

# # Fetch data from SQL
# data = pd.read_sql(query, engine)

# # Create scatter plot
# plt.figure(figsize=(10, 6))
# plt.scatter(data["Sales"], data["Profit"], alpha=0.5)

# # Add title and labels
# plt.title("Sales vs Profit")
# plt.xlabel("Sales")
# plt.ylabel("Profit")

# # Add zero-profit reference line
# plt.axhline(y=0, linestyle="--")

# # Adjust layout
# plt.tight_layout()

# # Save chart
# plt.savefig("visualizations/sales_vs_profit.png", dpi=300)

# # Display chart
# plt.show()

# print("Sales vs Profit chart saved successfully!")
# Step 22: Sales Distribution Histogram

# query = """
# SELECT
#     Sales
# FROM superstore;
# """

# # Fetch data from SQL
# data = pd.read_sql(query, engine)

# # Create histogram
# plt.figure(figsize=(10, 6))
# plt.hist(data["Sales"], bins=30, edgecolor="black")

# # Add title and labels
# plt.title("Sales Distribution")
# plt.xlabel("Sales Amount")
# plt.ylabel("Number of Orders")

# # Adjust layout
# plt.tight_layout()

# # Save chart
# plt.savefig("visualizations/sales_distribution.png", dpi=300)

# # Display chart
# plt.show()

# print("Sales Distribution chart saved successfully!")
