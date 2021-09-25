#!/usr/bin/env python
# coding: utf-8

# In[123]:


import pandas as pd  
import numpy as np 
import plotly.express as px

#coluna = 'A B C D E F G'.split()
#linha = 'ANA MARIA CARLOS LUCAS PEDRO MATHEUS LETICIA GABRIELA'.split()
#dados= np.random.randint(100,200,len(linha)*len(coluna)).reshape(len(linha),len(coluna))
 
#tabela = pd.DataFrame(data=dados,index=linha,columns= coluna)
#tabela

coluna = 'vendedor1 vendedor2 vendedor3 vendedor4 vendedor5'.split()
linhas ='dia1 dia2 dia3 dia4 dia5'.split()
dados = np.random.randint(10,25,len(coluna)*len(linhas)).reshape(len(linhas),len(coluna))

tabela = pd.DataFrame(data=dados,index=coluna,columns=linhas)
tabela


# In[48]:


tabela


# In[61]:


valores=[]
for indice,linha in tabela.iterrows():
    valores.append('bom' if linha['Soma'] <=100 else 'ruim')
tabela['ligacoes'] = valores
tabela


# In[64]:


tabela1= pd.DataFrame(tabela)
tabela1


# In[69]:


tabela1['%'] = (tabela1['dia1']+tabela1['dia2']+tabela1['dia3']+tabela1['dia4']+tabela1['dia5']) / 5
tabela1


# In[100]:


linha= 'ana lucas carlos renato bia'.split()
coluna = 'solteiros'.split()
dados = np.random.randint(0,2,len(coluna)*len(linha)).reshape(len(linha),len(coluna))
                                 

tabela2 = pd.DataFrame(data=dados,index=linha,columns=coluna)
tabela2


# In[104]:


valor=[]
for indice,linha in tabela2.iterrows():
    valor.append('solteiro' if linha['solteiros'] ==0 else 'namorando')
tabela2['estado_civil']=valor
tabela2


# In[125]:


tabela2['colunaNova'] = 'Ruim' #atribui o valor de ruim para todos no primeiro momento
tabela2.loc[tabela2['estado_civil'].isin(['solteiro']),'colunaNova']= 'Bom'
tabela2.loc[tabela2['estado_civil'].isin(['namorando']),'colunaNova']= 'Ruim'
tabela2


# In[134]:


px.bar(tabela2,x='colunaNova',color='estado_civil')

