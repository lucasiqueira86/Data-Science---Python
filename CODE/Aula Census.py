#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px 


# In[35]:


base_census = pd.read_csv(r'C:\Users\Master\Desktop\Jupyter\IA UDEMY\census.csv')
base_census


# In[36]:


base_census.describe()


# In[37]:


base_census.isnull().sum()# verificando se ha dados faltantes


# In[38]:


np.unique(base_census['income'], return_counts=True);


# In[39]:


sns.countplot(x = base_census['income']);


# In[41]:


plt.hist(x =base_census['age']);


# In[42]:


plt.hist(x = base_census['education-num']);


# In[43]:


plt.hist(x = base_census['hour-per-week']);


# In[16]:


grafico = px.treemap(base_census,path=['occupation','relationship'])
grafico.show()


# In[ ]:





# In[44]:


grafico = px.parallel_categories(base_census,dimensions=['occupation','relationship','income'])
grafico.show()

#grafico = px.parallel_categories(base_census,dimensions=['workclass','occupation','income'])
#grafico.show()
# In[45]:


x_census = base_census.iloc[:,0:14].values
y_census = base_census.iloc[:, 14].values


# In[10]:


#label Encoder = serve para deixar os numeros proporcionais
from sklearn.preprocessing import LabelEncoder


# In[49]:


label_encoder_workclass = LabelEncoder()
label_encoder_education= LabelEncoder()
label_encoder_marital = LabelEncoder()
label_encoder_occupation=LabelEncoder()
label_encoder_relationship= LabelEncoder()
label_encoder_race = LabelEncoder()
label_encoder_sex = LabelEncoder()
label_encoder_country = LabelEncoder()

x_census[:,1 ] = label_encoder_workclass.fit_transform(x_census[:,1])
x_census[:,3 ] = label_encoder_education.fit_transform(x_census[:,3])
x_census[:,5 ] = label_encoder_marital.fit_transform(x_census[:,5])
x_census[:,6 ] = label_encoder_occupation.fit_transform(x_census[:,6])
x_census[:,7 ] = label_encoder_relationship.fit_transform(x_census[:,7])
x_census[:,8 ] = label_encoder_race.fit_transform(x_census[:,8])
x_census[:,9 ] = label_encoder_sex.fit_transform(x_census[:,9])
x_census[:,13] = label_encoder_country.fit_transform(x_census[:,13])


# In[58]:


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

onehotencoder_census = ColumnTransformer(transformers=[('OneHot',OneHotEncoder(), [1,3,5,7,8,9,13])],remainder='passthrough')
x_census = onehotencoder_census.fit_transform(x_census).toarray() #toarray() transforma para o numpyarray
x_census


# In[ ]:





# In[ ]:





# In[ ]:




