#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Assignment 1: Data Exploration
Tasks:
1.	Load the banking_data.csv file using Pandas.
2.	Display the first 5 rows of the dataset.
3.	Use .describe() to generate basic statistics of the numerical columns (e.g., Transaction_Amount, Account_Balance).
4.	Check for missing values in the dataset.
Objective:
•	Understand how to load and inspect the dataset.
•	Use basic descriptive statistics and data integrity checks.
________________________________________
Assignment 2: Data Aggregation and Grouping
Tasks:
1.	Group the data by Account_Type and calculate:
o	The total sum of Transaction_Amount.
o	The average Account_Balance for each account type.
2.	Group the data by Branch and calculate:
o	The total number of transactions per branch.
o	The average transaction amount per branch.
"""


# In[4]:


import pandas as pd 
df=pd.read_csv(r'C:\dataset\Day_9_banking_data.csv')
df


# In[5]:


df.head(5)


# In[6]:


df.describe()


# In[7]:


df.isnull()


# In[8]:


df.groupby('Account_Type')['Transaction_Amount'].sum()


# In[9]:


df.groupby('Account_Type')['Account_Balance'].mean()


# In[10]:


df.groupby('Branch')['Transaction_Type'].count()


# In[11]:


df.groupby('Branch')['Transaction_Amount'].mean()


# In[ ]:




