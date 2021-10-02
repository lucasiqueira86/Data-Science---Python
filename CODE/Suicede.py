#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import plotly.express as px
import seaborn as sb
import numpy as np
from jupyterthemes import jtplot 
jtplot.style()
get_ipython().system('jt -t monokai -f fira -fs 12 -nf ptsans -nfs 12 -N -kl -cursw 2 -cursc r -cellw 90% -ofs 12 -dfs 12 -T')


sui = pd.read_csv(r'C:/Users/Master/Desktop/Jupyter/Suicidio1985.csv')

sui.describe()


# In[4]:


sui


# In[5]:


sui.head(10)


# In[4]:


sui.tail(60)


# In[6]:


np.unique(sui['country'],return_counts = True)


# In[6]:


sui['country'].value_counts()


# In[7]:


np.unique(sui['generation'],return_counts=True)


# In[8]:


sui['suicides_no'].sum()


# In[9]:


sb.countplot(x=sui['generation']);


# In[10]:


countrySelect = sui.query('country ==["Brazil","United States"]')
countrySelect


# In[11]:


np.unique(countrySelect['country'],return_counts= True)


# In[12]:


np.unique(countrySelect['sex'],return_counts=True)


# In[13]:


countrySelect['sex']


# In[14]:


px.bar(countrySelect,x='year',y='suicides_no',color='country')


# In[97]:


px.bar(countrySelect,x='year',y='population',color='country')


# In[100]:


px.bar(countrySelect,x='year', y='generation',color='country')


# In[17]:


sb.pairplot(countrySelect,vars =['year','suicides_no','population'] ,hue='country');

