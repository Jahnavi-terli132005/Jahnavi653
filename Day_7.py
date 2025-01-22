#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv(r'C:\dataset\Day_7_sales_data.csv')
df


# In[3]:


df[df['Sales']>1000]


# In[6]:


df['Profit_Per_Unit']=df['Profit']/df['Quantity']
df


# In[11]:


df['High_Sales']=((df['Sales']>1000)=='Yes')
df


# In[ ]:




