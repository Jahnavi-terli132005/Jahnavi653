#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Assignment 1: Data Visualization
Tasks:
1.	Plot the total sum of Transaction_Amount per Account_Type using a bar plot.
2.	Create a pie chart to show the percentage of transactions per Branch.
"""


# In[1]:


import pandas as pd
df=pd.read_csv(r'C:\dataset\Day_9_banking_data.csv')
df


# In[3]:


import matplotlib.pyplot as plt
fr=df.groupby('Account_Type')['Transaction_Amount'].sum()
fr.plot(kind='bar', figsize=(8, 5))
plt.title('Total Transaction Amount per Account Type')
plt.xlabel('Account Type')
plt.ylabel('Total Transaction Amount')
plt.show()


# In[11]:


fr = df['Branch'].value_counts()
plt.pie(fr, labels=fr.index, autopct='%1.1f%%', startangle=0)
plt.title('Percentage of Transactions per Branch')
plt.show()

