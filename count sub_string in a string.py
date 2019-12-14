#!/usr/bin/env python
# coding: utf-8

# In[13]:


def count_sub_string(string,sub_string):
    s=0
    for i in range(0,len(string)):
        if (string[i:len(sub_string)+i]==sub_string):
                s=s+1
    return s
string=input("enter the string here:")
sub_string=input("enter the sub string here:")
print(count_sub_string(string,sub_string))


# In[ ]:





# In[ ]:





# In[ ]:




