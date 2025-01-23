#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""1.	Load and Explore the Data
o	Load the sales_data.csv file using Pandas.
o	Display the first 5 rows of the dataset.
o	Print basic statistics (mean, median, min, max, etc.) of the numerical columns using .describe().
2.	Data Analysis
o	Calculate the total sales for each region.
o	Find the most sold product (based on quantity).
o	Compute the average profit margin for each product. (Profit margin = Profit / Sales * 100)
"""


# In[1]:


import pandas as pd
df=pd.read_csv(r'C:\dataset\Day_7_sales_data.csv')
df


# In[2]:


df.head(5)


# In[3]:


df.describe()


# In[4]:


total=df.groupby('Region')['Sales'].sum()
total


# In[11]:


total_quantity_by_product = df.groupby('Product')['Quantity'].sum()

most_sold_product = total_quantity_by_product.idxmax()
print("Most Sold Product:", most_sold_product)


# In[14]:


avg=df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
average = df.groupby('Product')['Profit_Margin'].mean()
print("Average Profit Margin by Product:\n", average)

