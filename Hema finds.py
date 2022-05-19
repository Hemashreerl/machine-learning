#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[13]:


data = pd.read_csv("play.csv")


# In[20]:


data


# In[21]:


concept=np.array(data)[:,0:-1]


# In[22]:


concept


# In[23]:


target=np.array(data)[:,-1]

   


# In[24]:


target


# In[25]:


def train(c,t):
    for i,val in enumerate(t):
        if val=="yes":
            hypothesis=c[i].copy()
            break
            
    for i,val in enumerate(concept):
        if t[i]=="yes":
            for x in range(len(hypothesis)):
                if val[x]!=hypothesis[x]:
                    hypothesis[x]='?'
                else:
                    pass
                
    return hypothesis


# In[26]:


train(concept,target)


# In[ ]:




