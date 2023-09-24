#!/usr/bin/env python
# coding: utf-8

# In[4]:


str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)


# In[9]:


str3 = '123'
x=int(str3)+1
print(x)


# In[10]:


fruit = 'banana'
letter = fruit[1]
print(letter)


# In[15]:


fruit= 'apple'
letter = fruit[4]
print(letter)


# In[17]:


fruit= 'apple'
print (len(fruit))


# In[18]:


#Looping Through Strings (while loop)


# In[19]:


fruit = 'banana'
index = 0
while index < len(fruit): 
    letter = fruit[index]
    print(index, letter)
    index = index + 1


# In[20]:


fruit = 'apple'
index = 0
while index <len(fruit):
    letter= fruit[index]
    print(index,letter)
    index= index + 1


# In[21]:


#For  loop 


# In[23]:


fruit = 'banana'
for letter in fruit: 
    print(letter)


# In[24]:


fruit ='pineapple'
for i in fruit:
    print(i)


# In[26]:


word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
    print(count)


# In[27]:


word = 'pineapple'
count = 0
for i in word:
    if i=='a':
        count = count +1
    print(count)


# In[28]:


#Slicing Strings


# In[32]:


s = 'Monty Python'
print(s[0:4])


# In[34]:


s='Loblolly pine is one of the most planted forest tree species in the Southern United States for sawtimber production'
print(s[3:10])


# In[36]:


print(s[9:15])


# In[38]:


print(s[ :20])


# In[39]:


print(s[30: ])


# In[40]:


#Using in as a Logical Operator


# In[41]:


fruit = 'banana'
'n' in fruit


# In[44]:


fruit= 'Apple'
'i' in fruit


# In[46]:


if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')


# In[48]:


greet = 'Hello Bob'
zap = greet.lower()
print(zap)


# In[52]:


string='Loblolly pine is one of the most planted forest tree species in the Southern United States for sawtimber production'
a=string.find("t")
print(a)


# In[54]:


A=string.upper()
print(A)


# In[57]:


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)


# In[64]:


data = 'hinaali128@books.library.gmail.com jan'
a= data.find('@')
print(a)
s=data.find('.',a)
print(s)
host= data[a+1:s]
print(host)


# In[ ]:




