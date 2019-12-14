#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
#check if the strings starts with "The" and ends with "Spain"
txt="The rain in Spain"
x=re.search("^The.*Spain$",txt)
if(x):
    print("YES!! we have a match")
else:
    print("no match")


# In[3]:


import re
str1="The rain in spain"
x=re.findall("ai",str1)
print(x)


# In[4]:


import re
str1="The rain in spain"
x=re.search('\s',str1)
print("the first white_space character is located at:",x.start())


# In[5]:


import re
str1="The rain in spain"
x=re.split("\s",str1)
print(x)


# In[6]:


import re
str1="The rain in spain"
x=re.split("\s",str1,1)
print(x)


# In[7]:


import re
str1="The rain in spain"
x=re.sub("\s","9",str1)
print(x)


# In[8]:


import re
str1="The rain in spain"
x=re.sub("\s","9",str1,2)
print(x)


# In[9]:


import re
str1="The rain in spain"
x=re.search('ai',str1)
print(x)


# In[10]:


print(x.start())


# In[11]:


print(x.span())


# In[12]:


print(x.string)


# In[13]:


print(x.group())


# In[16]:


import re
str1="The rain in Spain"
x=re.search('S.*$',str1)
print(x.span())


# In[18]:


import re
str1="The rain in spain"
x=re.findall('[a-m]',str1)
print(x)


# In[19]:


import re
str1="That will be 59 dollars"
x=re.findall('\d',str1)
print(x)


# In[25]:


import re
str1="hello world"
x=re.findall("^he..o",str1)
print(x)


# In[2]:


import re
str1="The rain in Spain"
x=re.search('\AThe',str1)
if (x):
    print("yes the string starts with The")
else:
    print("no match")


# In[3]:


import re
str1="The rain in Spain"
x=re.findall('\AThe',str1)
print(x)
if (x):
    print("yes the string starts with The")
else:
    print("no match")


# In[6]:


import re
str1="The rain in Spain"
x=re.findall('\bain',str1)
print(x)
if(x):
    print("yes present")
else:
    print("not present")


# In[8]:


import re
str1="The rain in Spain"
x=re.findall(r'ain\b',str1)
print(x)
if(x):
    print("yes present")
else:
    print("not present")


# In[11]:


import re
str1="The rain in Spain"
x=re.findall(r'\Bain',str1)
print(x)
if(x):
    print("yes present")
else:
    print("not present")


# In[12]:


import re
str1="The rain in Spain"
x=re.findall('[arn]',str1)
print(x)


# In[13]:


import re
str1="The rain in Spain"
x=re.findall('[a-n]',str1)
print(x)


# In[14]:


import re
str1="The rain in Spain"
x=re.findall('[^arn]',str1)
print(x)


# In[15]:


import re
str1="The rain in Spain"
x=re.findall('[+]',str1)
print(x)


# In[17]:


import re
line="cats are smarter than dogs"
x=re.match(r'(.*) are (.*).*',line)
if x:
    print(x.group())
    print(x.group(1))
    print(x.group(2))


# In[ ]:




