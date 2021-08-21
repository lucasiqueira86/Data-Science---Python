#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sb

depressed = pd.read_csv(r'C:/Users/Master/Desktop/Jupyter/depressed.csv')

#depressed: [ Zero: No depressed] or [One: depressed] 
#married zero : No married  or 1: Married
# Sex 0: Man 1:Women


# In[61]:


depressed


# In[62]:


np.unique(depressed['sex'],return_counts=True)


# In[63]:


np.unique(depressed['Married'],return_counts = True)
#0   No married  = 117 
#1   Married = 1104


# In[64]:


depressed['Number_children'].mean()


# In[65]:


depressed['gained_asset'].mean()


# In[66]:


np.unique(depressed['depressed'],return_counts= True)
#[ Zero: No depressed]  = 1191
#[One: depressed] = 238


# In[67]:


sb.countplot(x=depressed['sex']);


# In[68]:


sb.countplot(x=depressed['Married']);


# In[69]:


sb.countplot(x=depressed['depressed']);


# In[70]:


#Man with depression
man = depressed.query('sex=="0" & depressed=="1"')
man


# In[71]:


man['Age'].value_counts()


# In[72]:


woman = depressed.query('sex=="1" & depressed=="1"')
woman


# In[78]:


womandepre = woman['Age'].value_counts()
womandepre


# In[77]:


depressed.drop('labor_primary', axis=1)

