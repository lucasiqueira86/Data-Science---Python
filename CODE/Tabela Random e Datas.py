#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd  
import numpy as np 

coluna = 'A B C D E F G'.split()
linha = 'ANA MARIA CARLOS LUCAS PEDRO MATHEUS LETICIA GABRIELA'.split()
dados= np.random.randint(100,200,len(linha)*len(coluna)).reshape(len(linha),len(coluna))
 
tabela = pd.DataFrame(data=dados,index=linha,columns= coluna)
tabela


# In[19]:


coluna1 = 'DIA1 DIA2 DIA3 DIA4 DIA5'.split()
linhas1 = 'VENDEDOR1 VENDEDOR2 VENDEDOR3 VENDEDOR4 VENDEDOR5 VENDEDOR6 VENDEDOR7'.split()
dados1 = np.random.randint(10,100,len(linhas1)*len(coluna1)).reshape(len(linhas1), len(coluna1))
tabela1 = pd.DataFrame(data=dados1,index=linhas1,columns=coluna1)
tabela1


# In[26]:


data3 =pd.date_range('01-01-2020','30-12-2020')
len(data3)


# In[28]:


data3


# In[33]:


tabela5 = pd.DataFrame(data3)
tabela5


# In[49]:


tabela5[0].dt.day


# In[52]:


tabela5[0].dt.month


# In[54]:


tabela5[0].dt.year


# In[57]:


tabela5[0].dt.weekday


# In[58]:


tabela5[0].dt.day_name()


# In[59]:


#trimestre
tabela5[0].dt.quarter

