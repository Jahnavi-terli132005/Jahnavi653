#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Assignment 1: Sorting and Ranking Data
Tasks:
1.	Sort the dataset by Account_Balance in descending order and display the first 10 rows.
2.	Create a ranking column for Transaction_Amount within each Branch:
o	Use rank() to give ranks for transactions based on their amounts within each branch.
"""


# In[1]:


import pandas as pd
df=pd.read_csv(r'C:\dataset\Day_9_banking_data.csv')
df


# In[5]:


df.sort_values(by='Account_Balance',ascending=False)
df.head(10)


# In[6]:


df['Rank']=df.groupby('Branch')['Transaction_Amount'].rank()


# In[7]:


df

