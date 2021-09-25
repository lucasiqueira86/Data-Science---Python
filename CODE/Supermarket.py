#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sb
import plotly.express as pl
import numpy as np


super = pd.read_csv(r'C:\Users\Master\Desktop\Jupyter\supermarket_sales.csv')
super.describe()


# In[6]:


super


# In[9]:


super.value_counts('City')


# In[13]:


sb.countplot(x=super['City']);


# In[16]:


super.value_counts('Gender')


# In[18]:


sb.countplot(x=super['Gender']);


# In[21]:


super.value_counts('Product line')


# In[25]:


sb.countplot(x=super['Product line']);


# In[27]:


super.value_counts('Payment')


# In[53]:


sb.countplot(x=super['Payment']);


# In[56]:


super.value_counts('Customer type')


# In[58]:


sb.countplot(x=super['Customer type']);


# In[45]:


health = super[super['Product line'].isin(['Health and beauty'])]
health


# In[46]:


health.value_counts('Gender')


# In[47]:


sb.countplot(x=health['Gender']);


# In[50]:


health.value_counts('Payment')


# In[59]:


sb.countplot(x=super['Payment']);


# In[78]:


date = super['Date']
date
tabela = pd.DataFrame(date)
tabela


# In[112]:


#tabelaDate = tabela['Date'].astype('datetime64')
tabelaDate = pd.to_datetime(tabela['Date'])
tabelaDate


# In[120]:


name = tabelaDate.dt.day_name()
name


# In[123]:


df= pd.DataFrame(tabelaDate)
df


# In[164]:


df.rename(columns={'nameDay1':'DayName'})







# In[168]:


#drop() apaga colunas e linhas.
df.drop(1)


# In[110]:


tabelaDate.dt.dayofyear


# In[111]:


tabelaDate.dt.days_in_month

