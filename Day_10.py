#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Assignment 1: Filtering Data Based on Conditions
Tasks:
1.	Filter out all rows where the Transaction_Amount is greater than 2000.
2.	Find all rows where the Transaction_Type is "Loan Payment" and the Account_Balance is greater than 5000.
3.	Extract transactions made in the "Uptown" branch.
Objective:
•	Practice filtering data using conditions and boolean indexing.
________________________________________
Assignment 2: Data Transformation
Tasks:
1.	Add a new column called Transaction_Fee, calculated as 2% of Transaction_Amount.
2.	Create a new column Balance_Status:
o	If Account_Balance is greater than 5000, label it as "High Balance".
o	Otherwise, label it as "Low Balance".
"""


# In[2]:


import pandas as pd
df=pd.read_csv(r'C:\dataset\Day_9_banking_data.csv')
df


# In[5]:


df[df['Transaction_Amount']>2000]


# In[12]:


df[(df['Transaction_Type']=='Loan Payment') & (df['Account_Balance']>5000)]


# In[13]:


df[df['Branch']=='Uptown']


# In[15]:


df['Transaction_Fee']=df['Transaction_Amount']*0.02
df


# In[17]:


def balance_status(balance):
    if balance>5000:
        return 'High Balance'
    else:
        return 'Low Balance'
df['Balance_status']=df['Account_Balance'].apply(balance_status)
df

