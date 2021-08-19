#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sb

titanic = pd.read_csv(r'C:/Users/Master/Desktop/Jupyter/titanic_data.csv')

titanic.describe()


# In[7]:


titanic


# In[8]:


np.unique(titanic['Sex'],return_counts=True)


# In[9]:


sb.countplot(x=titanic['Sex']);


# In[ ]:





# In[11]:


titanic['Cabin'].isnull().sum()


# In[13]:


np.unique(titanic['Pclass'],return_counts=True)


# In[19]:


#Classes Ditribution
sb.countplot(x=titanic['Pclass']);


# In[21]:


np.unique(titanic['Survived'], return_counts=True)


# In[24]:


#Survived Distibution 
#0 not survived
#1=survived
sb.countplot(x=titanic['Survived']);


# In[29]:


np.unique(titanic['Sex'],return_counts=True)


# In[44]:


titanic.query('Sex=="male" & Survived==0')


# In[55]:


maleNOTsuvived = (468/577)*100
maleNOTsuvived                


# In[53]:


titanic.query('Sex=="female" & Survived==0')


# In[57]:


womanNOTsurvived  =(81/314)*100
womanNOTsurvived


# In[65]:


firstNOTSuvived = titanic.query('Pclass=="1" & Survived==0 ')
firstNOTSuvived


# In[68]:


np.unique(titanic['Pclass'],return_counts=True)


# In[70]:


FistNOTsurvived = (80/216)*100
FistNOTsurvived


# In[72]:


SecondNOTSuvived = titanic.query('Pclass=="2" & Survived==0 ')
SecondNOTSuvived


# In[74]:


SecondNOTsurvived = (97/184)*100
SecondNOTsurvived


# In[76]:


thirdNOTSuvived = titanic.query('Pclass=="3" & Survived==0 ')
thirdNOTSuvived


# In[78]:


thirdNOTsurvived = (97/184)*100
thirdNOTsurvived


# In[89]:


NotSurvived = {'passager':['First Classs','Second Classs','Third Class'], 'NotSuvived':[FistNOTsurvived,SecondNOTSuvived,thirdNOTsurvived]}
dataframe = pd.DataFrame(NotSurvived)
dataframe


# In[ ]:




