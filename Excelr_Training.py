#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import read_csv
from numpy import set_printoptions
from sklearn import preprocessing
path=r'C:\dataset\diabetes.csv'
names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
df=read_csv(path,usecols=names)
print(df)


# In[4]:


df=pd.read_csv(r'C:\dataset\diabetes.csv')
df


# In[5]:


df.head(250)


# In[10]:


df.info()


# In[7]:


print(df.describe())


# In[8]:


print(df.isnull().sum())


# In[14]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import read_csv
from numpy import set_printoptions
from sklearn import preprocessing
path=r'C:\dataset\customers-100.csv'
df=pd.read_csv('C:\dataset\customers-100.csv')


# In[15]:


df.iloc[5:61,5:7]


# In[17]:


df.head(10)
df.iloc[1:50,1:15]
data=df['First Name']=='Preston'
data


# In[19]:


data=df['Company']=='Vega-Gentry'
data


# In[16]:


import pandas as pd
data=pd.DataFrame({'Brand':['Maruti','Hyundai','Tata','Mahindra','Maruti','Hyundai','Renault','Tata','Maruti'],
                  'Year':[2012,2014,2011,2015,2012,2016,2014,2018,2019],
                  'Kmsdriven':[50000,30000,60000,25000,10000,46000,31000,15000,12000],
                  'city':['Gurgaon','Delhi','Mumbai','Delhi','Mumbai','Delhi','Mumbai','Chennai','Ghazizbad'],
                  'Mileage':[28,27,25,26,28,29,24,21,24]})
display(data)


# In[23]:


import pandas as pd
data1=pd.DataFrame({'Brand':['Maruti','Hero','Tata','Activa','BMW','Lambo','Ferrari'],
                  'customer_name':['Ramu','Ram','Raju','Raj','Priya','Rani','Preeti'],
                  'discount_amount':['50%','25%','55%','26%','2%','5%','3%']})

display(data1)


# In[27]:


inner_join=pd.merge(data,data1,on = 'Brand',how='inner')
inner_join


# In[28]:


inner_join=pd.merge(data,data1,on = 'Brand',how='outer')
inner_join


# In[29]:


inner_join=pd.merge(data,data1,on = 'Brand',how='left')
inner_join


# In[30]:


inner_join=pd.merge(data,data1,on = 'Brand',how='right')
inner_join


# In[17]:


display(data.loc[(data.Brand=='Maruti') & (data.Year==2012)])


# In[19]:


display(data.loc[(data.city=='Delhi') & (data.Kmsdriven<30000)])


# In[22]:


display(data['Kmsdriven'].mean())


# In[21]:


dict1={'Customer_id':[1,2,3,4,5,6],'Product':['Oven','Oven','Oven','Telivison','Telivison','Telivison']}
df1=pd.DataFrame(dict1)
df1


# In[23]:


dict2={'Customer_id':[2,4,6,7,8],'State':['California','Washington','Newyork','Texas','California']}
df2=pd.DataFrame(dict2)
df2


# In[26]:


inner_join=pd.merge(df1,df2,on = 'Customer_id',how='inner')
inner_join


# In[27]:


inner_join=pd.merge(df1,df2,on = 'Customer_id',how='outer')
inner_join


# In[28]:


inner_join.ffill()


# In[29]:


inner_join.bfill()


# In[30]:


inner_join=pd.merge(df1,df2,on = 'Customer_id',how='left')
inner_join


# In[31]:


inner_join=pd.merge(df1,df2,on = 'Customer_id',how='right')
inner_join


# In[36]:


"""create two dataframe with df1 with product and customer name as colums names 
df2 as price and product_name"""
dict1={'Product':['Oven','Fridge','TV','Car','AC','Bike'],
    'Customer_name':['Ram','Rahul','Prem','Preeti','Sree','Vani']}
df1=pd.DataFrame(dict1)
df1


# In[37]:


dict2={'Price':[25000,60000,150000,45000],
      'Product':['Oven','AC','Bike','TV']}
df2=pd.DataFrame(dict2)
df2


# In[38]:


inner_join=pd.merge(df1,df2,on = 'Product',how='inner')
inner_join


# In[39]:


inner_join=pd.merge(df1,df2,on = 'Product',how='outer')
inner_join


# In[40]:


inner_join=pd.merge(df1,df2,on = 'Product',how='left')
inner_join


# In[41]:


inner_join=pd.merge(df1,df2,on = 'Product',how='right')
inner_join


# In[1]:


import pandas as pd
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32]}
data2 = {'key': ['K1', 'K2', 'K3', 'K4'],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}
df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2)


# In[32]:


df.describe()


# In[4]:


df


# In[5]:


df1


# In[31]:


df1.describe()


# In[42]:


import numpy as np
array=np.arange(100).reshape(20,5)
print(array)
type(array)


# In[1]:


import pandas as pd
sales_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 103, 104, 101],
    'Amount': [250, 300, 400, 500, 600],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}
customer_data = {
    'CustomerID': [101, 102, 103, 104],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30, 35, 40, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
sales_df = pd.DataFrame(sales_data)
customers_df = pd.DataFrame(customer_data)

print("Sales DataFrame:")
print(sales_df.head())

print("\nShape of sales data:", sales_df.shape)  
print("\nSales data statistics:")
print(sales_df.describe()) 
print("Sales dataframe",sales_df)
print("customers_df",customers_df)



# In[4]:


merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)
merged_df.describe()


# In[5]:


merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='outer')
print("\nMerged DataFrame:")
print(merged_df)


# In[6]:


merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='left')
print("\nMerged DataFrame:")
print(merged_df)


# In[7]:


merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='right')
print("\nMerged DataFrame:")
print(merged_df)


# In[3]:


# 2. Merging data (Sales with Customer info)
merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)

# 3. Accessing data using `loc` and `iloc`
print("\nAccess data using `loc` (row 1):")
print(merged_df.loc[1])

print("\nAccess data using `iloc` (row 2):")
print(merged_df.iloc[2])

# 4. Handling Missing Values
# Let's introduce some missing data for demonstration
merged_df.loc[2, 'Age'] = None  # Introduce missing value in Age column
print(merged_df)
# Check for missing values
print("\nCheck missing values (isnull):")
print(merged_df.isnull().sum())

# Fill missing values with the mean (for Age column)
merged_df['Age'].fillna(merged_df['Age'].mean(), inplace=True)
print("\nData after filling missing values:")
print(merged_df)

# 5. Aggregation: Calculate the mean sales per customer
mean_sales = merged_df.groupby('CustomerName')['Amount'].mean()
print("\nMean sales per customer:")
print(mean_sales)


# In[3]:


import pandas as pd
import numpy as np
data={
    'square_feet_area':[6500,4500,np.nan,7800,3000,3800,9600,np.nan,6700,3400],
    'Year_built':[2003,1976,2001,np.nan,1998,2000,2006,1978,1950,np.nan],
    'over_all_condition':[5,8,6,7,np.nan,7,8,6,np.nan,7],
    'ready_to_move':['Yes','No','No',np.nan,'No','No',np.nan,'Yes','No','Yes'],
    'Sale_price':[200000,180000,215000,250000,210000,350000,410000,230000,175000,340000]
}
df=pd.DataFrame(data)


# In[4]:


df


# In[5]:


df.isnull()


# In[6]:


df.isnull().sum()


# In[13]:


df['square_feet_area'].fillna(df['square_feet_area'].mean(),inplace=True)
df['Year_built'].fillna(df['Year_built'].mean(),inplace=True)
df['over_all_condition'].fillna(df['over_all_condition'].mean(),inplace=True)
df


# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(10)
data=pd.DataFrame({
    'value':np.concatenate([np.random.normal(0,1,100),np.random.normal(10,1,10)])    
})
Q1=data['value'].quantile(0.29)
Q3=data['value'].quantile(0.71)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers=data[(data['value']<lower_bound)|(data['value']>upper_bound)]
outliers
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
sns.boxplot(x=data['value'])
plt.title('Box Plot')
plt.subplot(1,2,2)
sns.violinplot(x=data['value'])
plt.title('Violin Plot')


# In[ ]:




