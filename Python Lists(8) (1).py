#!/usr/bin/env python
# coding: utf-8

# In[14]:


print([1, 24, 76])


# In[16]:


print(['hina', 'akbar', 'Ali'])


# In[18]:


for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')


# In[20]:


for i in ['hina','Akbar','Ali']:
    print(i)
print ('NAME')


# In[21]:


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')


# In[24]:


Name = ['hina','akbar','Ali']
for i in Name:
    print('my name is:',i)
print('its done')


# In[25]:


#Lists are Mutable


# In[27]:


fruit = 'Banana'
fruit[0] = 'B'


# In[35]:


fruit = ['Banana', 'Apple','gRapes']
fruit[0]=2
print(fruit)


# In[36]:


greet = 'Hello Bob'
print(len(greet))


# In[37]:


x = [ 1, 2, 'joe', 99]
print(len(x))


# In[40]:


friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))


# In[41]:


print(range(len(friends)))


# In[44]:


Name = ['h', 'i', 'n','a']
for i in Name :
    print('my name is:', i)
for j in range(len(Name)) :
    i = Name[j]
    print('name is here:', i)


# In[45]:


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b


# In[46]:


print(c)


# In[48]:


t = [9, 41, 12, 3, 74, 15]
t[1:3]


# In[49]:


t[:4]


# In[50]:


t[3:]


# In[52]:


x = list()
type(x)
dir(x)


# In[53]:


stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)


# In[55]:


animal=list()
animal.append('cat')
animal.append('dog')
animal.append('4')
print(animal)


# In[56]:


#Lists are in Order


# In[57]:


friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends)
print(friends[1])


# In[59]:


nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


# In[61]:


total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value 
    count = count + 1
average = total / count
print('Average:', average)


# In[66]:


total = 0
count = 0
while True:
    inp=input('enter num')
    if inp =='done':break
    value =float(inp)
    total = total+value
    count = count+1
average = total /count
print('average',average)


# In[67]:


numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)


# In[68]:


abc = 'With three words'
stuff = abc.split()
print(stuff)


# In[69]:


b = len(stuff)
print(b)


# In[73]:


line ='first;second;third'
thing = line.split(';')
print(thing)


# In[75]:


line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)


# In[77]:


words = line.split()
email = words[1]
print(email)


# In[80]:


words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces)


# In[ ]:




