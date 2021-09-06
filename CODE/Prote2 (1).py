#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import plotly.express as px
import plotly as pl
import seaborn as sb


prote = pd.read_excel(r'C:/Users/Master/Desktop/Jupyter/Prote2.xlsx')


# In[2]:


prote.describe()


# In[42]:


prote


# In[44]:


prote['PREÇO'].mean()


# In[47]:


prote['QUANTIDADE'].value_counts()


# In[49]:


sb.countplot(x=prote['QUANTIDADE']);


# In[3]:


np.unique(prote['PRODUTO'],return_counts=True)


# In[4]:


sb.countplot(x=prote['PRODUTO']);


# In[5]:


np.unique(prote['FORMA PGTO'],return_counts= True)


# In[6]:


sb.countplot(x=prote['FORMA PGTO']);


# In[8]:


maiorCompra = prote['TOTAL'].max()
maiorCompra


# In[9]:


prote[prote['TOTAL']==390.0]


# In[10]:


menorCompra = prote['TOTAL'].min()
menorCompra


# In[11]:


prote[prote['TOTAL']==56.9]


# In[12]:


prote['QUANTIDADE'].max()


# In[13]:


maiorQuantidade = prote[prote['QUANTIDADE']==4]
maiorQuantidade


# In[20]:


grafico1 = px.scatter(prote, x='TOTAL' , y='FORMA PGTO')
grafico1


# In[24]:


grafico0 = px.scatter_matrix(prote,dimensions=['TOTAL','FORMA PGTO','PRODUTO','PREÇO'],color='PRODUTO')
grafico0


# In[33]:


bar = px.bar(prote,x='DATA ', y='PRODUTO',color='PRODUTO')
bar 

