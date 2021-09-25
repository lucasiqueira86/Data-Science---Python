#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd  
import numpy as np 
import seaborn as sns

df = sns.load_dataset('diamonds')
df


# In[19]:


valores = []
for indice, linha in df.iterrows():
    valores.append('barato' if linha ['price'] <=100 else 'caro')
df['custo'] = valores
df
    
    

