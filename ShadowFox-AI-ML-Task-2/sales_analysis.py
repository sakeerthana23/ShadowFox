import pandas as pd

# Load the dataset with the specified encoding
df = pd.read_csv('Sample - Superstore.csv', encoding='ISO-8859-1')

# Print column names to check for any discrepancies
print(df.columns)

# Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values (optional)
df.dropna(inplace=True)

# Extract month and year from the 'Order Date' column
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# Print first few rows to confirm changes
print(df.head())

# Group by Month and Year to analyze sales trends
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

# Plot the sales trends
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['Year'].astype(str) + '-' + monthly_sales['Month'].astype(str), monthly_sales['Sales'], marker='o')
plt.title('Monthly Sales Trends')
plt.xlabel('Month-Year')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Group by Category and Sub-Category
category_sales = df.groupby(['Category', 'Sub-Category'])[['Sales', 'Profit']].sum().reset_index()

# Sort by sales to identify top performers
category_sales = category_sales.sort_values(by='Sales', ascending=False)

# Plot the top-performing categories and sub-categories
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.barplot(x='Sales', y='Sub-Category', hue='Category', data=category_sales)
plt.title('Sales by Product Category and Sub-Category')
plt.xlabel('Sales')
plt.ylabel('Sub-Category')
plt.show()

# Calculate profit margin
df['Profit Margin'] = df['Profit'] / df['Sales']

# Group by Category and Sub-Category to analyze profitability
profitability = df.groupby(['Category', 'Sub-Category'])['Profit Margin'].mean().reset_index()

# Plot the profitability
plt.figure(figsize=(12, 6))
sns.barplot(x='Profit Margin', y='Sub-Category', hue='Category', data=profitability)
plt.title('Profitability by Product Category and Sub-Category')
plt.xlabel('Profit Margin')
plt.ylabel('Sub-Category')
plt.show()

# Group by the 'Segment' column instead of 'CustomerSegment'
customer_sales = df.groupby('Segment')[['Sales', 'Profit']].sum().reset_index()

# Plot the sales by customer segment
plt.figure(figsize=(8, 5))
sns.barplot(x='Segment', y='Sales', data=customer_sales)
plt.title('Sales by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Sales')
plt.show()

