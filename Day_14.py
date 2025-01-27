#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Assignment 2: Drug Effectiveness and Side Effects Comparison
Objective:
Compare drug effectiveness and side effects by different products, regions, and trial periods. Visualize these comparisons using matplotlib and seaborn.
Instructions:
1.	Load the dataset.
2.	Perform any necessary data cleaning.
3.	Create the following visualizations:
o	A bar plot comparing the average Effectiveness for each drug across different regions.
o	A violin plot to show the distribution of Effectiveness and Side_Effects for each product.
o	A pairplot to explore relationships between Effectiveness, Side_Effects, and Marketing_Spend.
o	A boxplot comparing Effectiveness for different trial periods.
o	A regression plot to analyze how Marketing_Spend affects drug Effectiveness.
4.	Based on the visualizations, provide an analysis of:
o	Which product has the best overall effectiveness.
o	The correlation between effectiveness and side effects.
"""


# In[1]:


import pandas as pd
df=pd.read_csv(r'C:\dataset\Day_13_Pharma_data.csv')
df


# In[3]:


import pandas as pd

# Load the dataset
data = pd.read_csv('C:\dataset\Day_13_Pharma_data.csv')





# Check for missing values
print(data.isnull().sum())

# Check for duplicates
print(data.duplicated().sum())

# Drop any rows with missing values or duplicates
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)





import matplotlib.pyplot as plt
import seaborn as sns

# Group by Region and calculate total sales
region_sales = data.groupby('Region')['Sales'].sum().reset_index()

# Create bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=region_sales)
plt.title('Total Sales per Region')
plt.show()




plt.figure(figsize=(10, 6))
sns.scatterplot(x='Marketing_Spend', y='Sales', data=data)
plt.title('Relationship between Marketing Spend and Sales')
plt.show()




# Create boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age_Group', y='Effectiveness', data=data)
plt.title('Drug Effectiveness across Age Groups')
plt.show()






# Group by Product and Trial Period, and calculate total sales
product_sales = data.groupby(['Product', 'Trial_Period'])['Sales'].sum().reset_index()

# Create line plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='Trial_Period', y='Sales', hue='Product', data=product_sales)
plt.title('Sales Trend for Each Product')
plt.show()






# Calculate correlation matrix
corr_matrix = data[['Sales', 'Marketing_Spend', 'Effectiveness']].corr()

# Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation between Sales, Marketing Spend, and Effectiveness')
plt.show()



# In[ ]:




