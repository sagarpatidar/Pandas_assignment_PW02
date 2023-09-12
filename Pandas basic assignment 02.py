#!/usr/bin/env python
# coding: utf-8

# # Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

# In[1]:


import pandas as pd

data = [4, 8, 15, 16, 23, 42]
series = pd.Series(data)
print(series)


# # Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# 
# 

# In[2]:


import pandas as pd

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
series = pd.Series(my_list)
print(series)


# # Q3. Create a Pandas DataFrame that contains the following data:

# In[3]:


import pandas as pd
data = {
    'Name' :['Alice','bob','claire'],
    'Age' :[25,30,27],
    'Gender': ['Female','Male','Female']
}
df = pd.DataFrame(data)
print (df)


# # What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.
# 

# In[4]:


''''As noted in the table, a Pandas Series is
a 1D array of data, but a single-column DataFrame 
is a 2D table with one column. The main distinction between the two is this
. For a single-column DataFrame, an index can be optional, but a Series has to 
have an index defined'''


# # What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# 

# In[5]:


''''1. head and tail . to see the data frame we can use
2. shape, size and info. two most basic function after reading data
    is to know the rows and column 
3. isna
4. Describe 
5. Nunique
6. Valuecounts
7. columns.'''
#Asume that ill upload the data 


# In[6]:


df =pd.read_csv('Algerian_forest_fires_dataset_UPDATE.csv')


# In[7]:


df.head()


# In[8]:


df.isna


# In[9]:


df.describe()


# In[10]:


df.tail(2)


# # What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# # you give an example of when you might use one of these functions?

# In[11]:


#There are three support fucntion , .shape(), info(), and .corr()


# In[22]:


df =pd.read_csv('Algerian_forest_fires_dataset_UPDATE.csv')


# In[25]:


df


# In[26]:


df.describe()


# In[27]:


df.head()


# In[28]:


df.tail()


# In[29]:


df.memory_usage()


# In[33]:


df.loc[:]


# # Which of the following is mutable in nature Series, DataFrame, Panel?

# In[37]:


''''DataFrames are both value and size-mutable
(A Series, by contrast, is only value-mutable,
 not size-mutable. The length of a Series cannot
 be changed although the values can be changed).'''


# # Create a DataFrame using multiple Series. Explain with an example.

# In[ ]:


import pandas as pd

# Creating three Series
names = pd.Series(['Alice', 'Bob', 'Charlie', 'David'])
ages = pd.Series([25, 30, 35, 28])
cities = pd.Series(['New York', 'San Francisco', 'Los Angeles', 'Chicago'])

# Combining the Series into a DataFrame
data = {'Name': names, 'Age': ages, 'City': cities}
df = pd.DataFrame(data)

# Printing the DataFrame
print(df)


# In[ ]:




