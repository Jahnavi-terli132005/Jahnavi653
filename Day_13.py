#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Assignment 1: Sales and Effectiveness Analysis
Objective:
Explore the relationship between marketing spend, sales, and drug effectiveness across different regions and age groups. Create visualizations using matplotlib and seaborn.
Instructions:
1.	Load the dataset.
2.	Perform data cleaning (check for missing values, duplicates).
3.	Create the following visualizations:
o	A bar plot showing total sales per region.
o	A scatter plot to visualize the relationship between Marketing_Spend and Sales.
o	A boxplot comparing drug effectiveness across different age groups.
o	A line plot showing the sales trend for each product over different trial periods.
o	A heatmap of the correlation between Sales, Marketing_Spend, and Effectiveness.
4.	Based on the visualizations, summarize any patterns or trends you observe.
"""


# In[2]:


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('C:\dataset\Day_13_Pharma_data.csv')

# Perform data cleaning
# Check for missing values
print(data.isnull().sum())

# Check for duplicates
print(data.duplicated().sum())

# Drop any rows with missing values or duplicates
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

# Create visualizations
# A bar plot showing total sales per region
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=data)
plt.title('Total Sales per Region')
plt.show()

# A scatter plot to visualize the relationship between Marketing_Spend and Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Marketing_Spend', y='Sales', data=data)
plt.title('Relationship between Marketing Spend and Sales')
plt.show()

# A boxplot comparing drug effectiveness across different age groups
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age_Group', y='Effectiveness', data=data)
plt.title('Drug Effectiveness across Age Groups')
plt.show()

# A line plot showing the sales trend for each product over different trial periods
plt.figure(figsize=(10, 6))
sns.lineplot(x='Trial_Period', y='Sales', hue='Product', data=data)
plt.title('Sales Trend for Each Product')
plt.show()

# A heatmap of the correlation between Sales, Marketing_Spend, and Effectiveness
corr_matrix = data[['Sales', 'Marketing_Spend', 'Effectiveness']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation between Sales, Marketing Spend, and Effectiveness')
plt.show()

# Summarize patterns or trends observed from the visualizations
print('Insights:')
print('1. Marketing spend has a positive impact on sales.')
print('2. Certain age groups have higher drug effectiveness.')
print('3. Sales are distributed unevenly across regions.')
print('4. Sales trend varies across products and trial periods.')
print('5. Correlation exists between sales, marketing spend, and effectiveness.')





# In[2]:


df.isnull()


# In[3]:


df.duplicated()


# In[ ]:




