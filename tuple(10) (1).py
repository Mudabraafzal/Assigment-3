#!/usr/bin/env python
# coding: utf-8

# In[2]:


x = ('Glenn', 'Sally', 'Joseph')
print(x[2])


# In[3]:


t = tuple()
dir(t)


# In[4]:


(0, 1, 2) < (5, 1, 2)


# In[5]:


(0, 1, 2000000) < (0, 3, 4)


# In[7]:


d = {'a':10, 'b':1, 'c':22}
d.items()
sorted(d.items())


# In[8]:


for k, v in sorted(d.items()):
    print(k, v)


# In[ ]:




