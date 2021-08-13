#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import plotly as px
import numpy as np
import plotly.express as pxe

pd.options.plotting.backend = "plotly"

arrest= pd.read_csv(r'C:\Users\Master\Desktop\Jupyter\IA UDEMY\USArrests.csv')
arrest.describe()


# In[4]:


arrest


# In[3]:


MaxRape = arrest.loc[arrest['Rape']==46.0]
MaxRape


# In[4]:


arrest1 = arrest.rename(columns={'Unnamed: 0':'State'})
arrest1
#numeric Percent urban population


# In[5]:


arrest.isnull().count()


# In[6]:


EstadoMaiorMurder = arrest1['Murder'].max()
EstadoMaiorMurder


# In[11]:


EstadoMenorMaiorNome = arrest1[arrest1['Murder']==17.4]
EstadoMenorMaiorNome


# In[12]:


EstadoMaiorAssalt= arrest1['Assault'].max()
EstadoMaiorAssalt


# In[13]:


EstadoMaiorAssaltNome = arrest1[arrest1['Assault']==337]
EstadoMaiorAssaltNome


# In[14]:


EstadoMaiorRape = arrest1['Rape'].max()
EstadoMaiorRape


# In[15]:


EstadoMaiorRapeNome = arrest1[arrest1['Rape']==46.0]
EstadoMaiorRapeNome


# In[16]:


MaiorEstadoUrban = arrest1['UrbanPop'].max()
MaiorEstadoUrban


# In[17]:


MaiorEstadoUrbanNome = arrest1[arrest1['UrbanPop']==91]
MaiorEstadoUrbanNome


# In[18]:


MenorUrban = arrest1['UrbanPop'].min()
MenorUrban


# In[19]:


MenorUrbanNome = arrest1[arrest1['UrbanPop']==32]
MenorUrbanNome


# arrest.plot(kind='line')

# In[20]:


arrest1.plot(title='Assasinatos por Estados', x='State', y='Murder', kind='bar')


# In[21]:


arrest1.plot(title = 'Estupros por Estado', x='State',y='Rape', kind='bar')


# In[83]:


arrest1.plot(title='Assalto por Estado', x='State',y='Assault', kind='bar')


# In[84]:


arrest1.plot(title='Urbanização por Estado', x='State', y='UrbanPop', kind='bar')


# In[ ]:




