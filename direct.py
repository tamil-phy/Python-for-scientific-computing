#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


n_trials = 4000
n_hits = 0


# In[3]:


for iter in range(n_trials):
    x,y = random.uniform(-1.0,1.0), random.uniform(-1.0,1.0)


# In[4]:


if x**2 + y**2 < 1.0:
    n_hits += 1


# In[6]:


print(4.0 * n_hits/float(n_trials))


# In[ ]:




