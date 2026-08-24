import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = "sample_-_superstore.xls"

df = pd.read_excel(file)

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset shape:")
print(df.shape)

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Category-wise Sales and Profit Analysis

category_analysis = df.groupby('Category')[['Sales', 'Profit']].sum()

print("\nCategory-wise Sales and Profit:")
print(category_analysis)

# Sub-Category-wise Sales and Profit Analysis

subcategory_analysis = df.groupby('Sub-Category')[['Sales', 'Profit']].sum()

print("\nSub-Category-wise Sales and Profit:")
print(subcategory_analysis.sort_values('Profit', ascending=False))

# Region-wise Sales and Profit Analysis

region_analysis = df.groupby('Region')[['Sales', 'Profit']].sum()

print("\nRegion-wise Sales and Profit:")
print(region_analysis.sort_values('Profit', ascending=False))

# Discount vs Profit Analysis

discount_analysis = df.groupby('Discount')['Profit'].sum()

print("\nDiscount-wise Profit:")
print(discount_analysis)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=discount_analysis.index,
    y=discount_analysis.values
)

plt.title("Discount vs Total Profit")
plt.xlabel("Discount")
plt.ylabel("Total Profit")
plt.tight_layout()

plt.savefig("discount_vs_profit.png")
plt.show()

# Monthly Sales and Profit Analysis

df['Month'] = df['Order Date'].dt.month

monthly_analysis = df.groupby('Month')[['Sales', 'Profit']].sum()

print("\nMonthly Sales and Profit:")
print(monthly_analysis)
plt.figure(figsize=(10, 5))

sns.lineplot(
    x=monthly_analysis.index,
    y=monthly_analysis['Sales'],
    marker='o'
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(range(1, 13))
plt.tight_layout()

plt.savefig("monthly_sales_trend.png")
plt.show()

# Sub-Category Profit Analysis Chart

subcat_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values()

plt.figure(figsize=(10, 6))

sns.barplot(
    x=subcat_profit.values,
    y=subcat_profit.index
)

plt.title("Profit by Sub-Category")
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")
plt.tight_layout()

plt.savefig("subcategory_profit.png")
plt.show()

# Top 10 Most Profitable Products

product_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False)

print("\nTop 10 Most Profitable Products:")
print(product_profit.head(10))

print("\nTop 10 Loss-Making Products:")
print(product_profit.tail(10))

# Quantity vs Profit Analysis

quantity_profit = df.groupby('Quantity')['Profit'].sum()

print("\nQuantity-wise Profit:")
print(quantity_profit)

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x='Quantity',
    y='Profit',
    data=df
)

plt.title("Quantity vs Profit")
plt.xlabel("Quantity Sold")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("quantity_vs_profit.png")
plt.show()

df.to_csv("superstore_mysql.csv", index=False)

print("CSV file created successfully!")
check = pd.read_csv("superstore_mysql.csv")

print("CSV shape:", check.shape)
print("CSV columns:")
print(check.columns.tolist())

print("\nFirst 5 rows:")
print(check.head())
# Remove the extra Month column before exporting to MySQL
df_mysql = df.drop(columns=["Month"], errors="ignore")

df_mysql.to_csv("superstore_mysql.csv", index=False)

print("MySQL CSV file created successfully!")
print("CSV shape:", df_mysql.shape)
print("CSV columns:", df_mysql.columns.tolist())