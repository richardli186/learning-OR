import numpy as np
import pandas as pd

df = pd.read_csv('DataCoSupplyChainDataset.csv', encoding = 'latin1')
#print(df.shape)
#print(df.head())
#print(df.columns.to_list())
#print(df.describe())

"""
Dataset Practice

1. Filtering — Keep only orders where Order Status is COMPLETE
2. New column — Create a shipping_delay column (actual minus scheduled shipping days)
3. groupby + mean — Which Order Region has the highest average Benefit per order?
4. value_counts — What are the top 3 most ordered Product Names?
5. Boolean masking — What percentage of orders have a discount rate above 10%?
6. sort_values — What are the 5 orders with the highest Order Profit Per Order?
7. str methods — How many unique Order Region values contain the word "Asia"?
8. datetime parsing — Which month had the most orders placed?
9. pivot_table — What is the average Sales per Shipping Mode and Customer Segment?
10. apply — Create a new column that labels each order as "Profitable" 
    or "Not Profitable" based on Benefit per order
11. isnull — How many missing values exist in each column?
12. corr — Which numeric columns are most correlated with Sales?
13. nunique — How many unique customers placed orders in each Market?
"""

#Filter rows to only include orders where Order Status is COMPLETE
print(df[df['Order Status'] == 'COMPLETE'])

#Create a new column for shipping delays
df['Shipping Delay'] = df['Days for shipping (real)'] - df['Days for shipment (scheduled)']
print(df['Shipping Delay'])

#Which Order Region has the highest average Benefit per order?
region_benefit_avg = df.groupby('Order Region')['Benefit per order'].mean()
print(region_benefit_avg.idxmax(), ':', region_benefit_avg.max())

#What percentage of orders were delivered late?
print((df['Delivery Status'] == 'Late delivery').mean() * 100, '%')

#What are the top 3 most ordered Product Names?
print(df['Product Name'].value_counts(ascending = False).iloc[:3])

#What percentage of orders have a discount rate above 10%?
print((df['Order Item Discount Rate'] > 0.1).mean() * 100, '%')

#What are the 5 orders with the highest Order Profit Per Order?
print(df['Order Profit Per Order'].sort_values(ascending = False).iloc[:5])

#How many unique Order Region values contain the word "Asia"?
asia_mask = df['Order Region'].str.contains('Asia')
print(df[asia_mask]['Order Region'].nunique())

#Which month had the most orders placed?
datetime = pd.to_datetime(df['order date (DateOrders)'])
print(datetime.dt.month.value_counts().idxmax())

#What is the average Sales per Shipping Mode and Customer Segment?
print(df.groupby(['Shipping Mode', 'Customer Segment'])['Sales'].mean())

#Create a new column that labels each order as "Profitable" 
#or "Not Profitable" based on Benefit per order
def profitability(num):
    """
    Determines the profitability of an order

    Inputs:
        - num: a real number representing the benefit of the order

    Returns the string 'Not Profitable' if num is 0 or less, returns 'Profitable' otherwise
    """
    if num <= 0:
        return 'Not Profitable'
    else:
        return 'Profitable'
df['Profitability'] = df['Benefit per order'].apply(profitability)
print(df['Profitability'])

#How many missing values exist in each column?
print(df.isnull().sum())

#Which numeric columns are most correlated with Sales?
numeric_col = df.select_dtypes(include='number')
print(numeric_col.corr()['Sales'].sort_values(ascending = False))

#How many unique customers placed orders in each Market?
print(df.groupby('Market')['Customer Id'].nunique())