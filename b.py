#!/usr/bin/env python
# coding: utf-8

# In[5]:


myDict = {'name': 'Kelzz', 'age': 20}
myDict['address'] = 'Medan'
print(myDict)


# In[6]:


# Travese Through a Dictionary

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
        
traverseDict(myDict)


# In[28]:


# Searching a Dictionary

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
        return 'The value does not exist'
    print(searchDict(myDict, 21))


# In[29]:


# Delete Dictionary

myDict.pop('name')


# In[30]:


print(myDict)


# In[31]:


# Sorted Method

myDict = {'eooooa': 1, 'ass': 2, 'uud': 3, 'sseo': 4, 'werwi': 5}
print(sorted(myDict, key=len))


# In[32]:


print(myDict)


# In[33]:


myDict.clear()


# In[34]:


print(myDict)


# In[35]:


myDict = {'name': 'Kelzz', 'age': 20}


# In[36]:


print(myDict)


# In[37]:


dict = myDict.copy()


# In[38]:


print(dict)


# In[39]:


newDict = {}.fromkeys([1,2,3], 0)
print(newDict)


# In[40]:


print(myDict.get('city', 20))


# In[41]:


print(myDict.get('city', 21))


# In[42]:


print(myDict.get('city'))


# In[44]:


print(myDict.get('name', 20))


# In[45]:


print(myDict.items())


# In[46]:


print(myDict.values())


# In[47]:


print(myDict.popitem())


# In[48]:


print(myDict)


# In[49]:


print(myDict.setdefault('name', 'added'))


# In[50]:


print(myDict.setdefault('name1', 'added'))


# In[51]:


print(myDict)


# In[52]:


newDict = {'a':1, 'b':2, 'c':3}
myDict.update(newDict)
print(myDict)


# In[ ]:




