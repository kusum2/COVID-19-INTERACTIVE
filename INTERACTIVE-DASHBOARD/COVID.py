#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
sns.set(color_codes=True)


# In[2]:


country = pd.read_csv('dataset.csv')


# In[3]:


country.head()


# In[4]:


country.info()


# In[5]:


sorted_country=country.sort_values('Confirmed',ascending=False).head(5)


# In[6]:


sorted_country


# In[7]:


def highlight_col(x):
    r = 'background-color: red'
    b = 'background-color: blue'
    g = 'background-color: green'
    temp=pd.DataFrame('', index=x.index, columns=x.columns)
    temp.iloc[:,1]=b
    temp.iloc[:,2]=r
    temp.iloc[:,3]=g
    return temp

sorted_country.head(5).style.apply(highlight_col, axis=None)
    


# In[8]:


sns.barplot(sorted_country['Deaths'],sorted_country['Country/Region'].head(5))


# In[9]:


sns.distplot(country['Active'])


# In[10]:


sns.jointplot(country['Confirmed'],country['Deaths'])


# In[11]:


sns.pairplot(country[['New cases','New deaths','New recovered']])


# In[12]:


sns.stripplot(country['Deaths / 100 Cases'],country['Recovered / 100 Cases'])


# In[13]:


sns.countplot(country['WHO Region'])


# In[14]:


import plotly.express as px


# In[15]:


fig= px.scatter(sorted_country.head(5),x='Country/Region',y='Confirmed',size='Confirmed',
              color='Country/Region', hover_name="Country/Region", size_max=50)
fig.show()


# In[ ]:


# 

