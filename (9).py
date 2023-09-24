#!/usr/bin/env python
# coding: utf-8

# In[1]:


purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)


# In[2]:


print(purse['candy'])


# In[3]:


lst = list()
lst.append(21)
lst.append(183)
print(lst)


# In[4]:


ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)


# In[5]:


ddd= dict()
ddd['name'] = 'Hina Ali'
ddd['course'] = '703'
print(ddd)


# In[7]:


ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)


# In[11]:


counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts: 
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)


# In[14]:


if name in counts:
    x = counts[name]
else :
    x = 0
x = counts.get(name, 0)
print(x)


# In[16]:


counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)


# In[17]:


counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)


# In[18]:


counts = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])


# In[23]:


jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(list(jjj))


# In[22]:


print(jjj.keys())


# In[24]:


print(jjj.values())


# In[25]:


print(jjj.items())


# In[26]:


jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for aaa,bbb in jjj.items() :
    print(aaa, bbb)


# In[ ]:


name = input('Enter file:')
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1


# In[ ]:




