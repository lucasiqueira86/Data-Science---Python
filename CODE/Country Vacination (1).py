#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly as pxe
import plotly.express as px

country = pd.read_csv(r'C:\Users\Master\Desktop\Jupyter\country_vaccinations.csv')
country.describe()


# In[2]:


country


# In[3]:


np.unique(country['country'],return_counts= True)


# In[4]:


Brazil = country.loc[country['country'] == 'Brazil']
Brazil


# In[5]:


country.isnull().sum()


# In[6]:


Brazil['daily_vaccinations'].max()


# In[7]:


#Day with mores peoople been vacinated
Brazil[Brazil['daily_vaccinations'] == 1520483.0]


# In[8]:


grafico1 = px.scatter(Brazil, x='date',   y='total_vaccinations', title='Comparation between number of vacines aplicated')
grafico1


# In[10]:


grafico2 = px.scatter(Brazil, x='date', y='people_fully_vaccinated', title='Comparation between date and fully vaccination people')
grafico2


# In[11]:


#Percent of peoople fully vacinated in Brazil
BrazilPopulation = 210
FullVaccination = 40
peooplevacc = FullVaccination/BrazilPopulation *100
peooplevacc


# In[12]:


grafico2 = px.scatter(Brazil, x='date', y='daily_vaccinations_per_million', title='Comparation between date and fully vaccination people per Million')
grafico2


# In[13]:


grafico3 = px.scatter(Brazil, x='date', y='people_fully_vaccinated_per_hundred', title='Comparation between date and fully vaccination people per Hundred')
grafico3


# In[14]:


EuaBrazil = country[country['country'].isin(['Brazil','United States'])]
EuaBrazil


# In[15]:


px.scatter(EuaBrazil,x='date',y='daily_vaccinations_per_million',title='Comparation between United States and Brazil',color='country')


# In[16]:




px.scatter(EuaBrazil, x='date', y='people_fully_vaccinated', title='Comparation between people fully vaccinated.EUA Population 328,2 milhões / Brazil Population 211 milhões',color='country')


# In[ ]:




