#!/usr/bin/env python
# coding: utf-8

# In[8]:


newTuple = ('a', 'b', 'c', 'd', 'e')
newTuple1 = tuple('abcde')
print(newTuple)


# In[9]:


print(newTuple1)


# In[10]:


#acces Tuple Elements
   
print(newTuple[0])


# In[13]:


print(newTuple[0])


# In[16]:


print(newTuple[4])


# In[18]:


print(newTuple[0:4])


# In[21]:


print(newTuple[0::3])


# In[23]:


print(newTuple[1::3])


# In[24]:


print(newTuple[:3])


# In[25]:


print(newTuple[-5])


# In[27]:


print(newTuple[-5::2])


# In[22]:


#traverse through tuple

for i in newTuple:
    print(i)


# In[37]:


for index in range(len(newTuple)):
    print(newTuple[index])


# In[38]:


# how to search for a element in tuple?

print('a' in newTuple)


# In[39]:


def searchInTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
        return 'The element does not exist'
    print(searchInTuple(newTuple, 'a'))


# In[41]:


# tuple operations

myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)
print(myTuple + myTuple1)


# In[42]:


print(myTuple * 4)


# In[43]:


print(2 in myTuple1)


# In[44]:


myTuple1.count(2)


# In[45]:


myTuple1.index(2)


# In[46]:


x, y, z = (10,15,20,25,30,35,40)[1::2]
print(x,y,z)


# In[49]:


x = 3
y = -6

x, y =(y, x)[::-1]
print(x, y)


# In[ ]:




