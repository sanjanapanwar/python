#!/usr/bin/env python
# coding: utf-8

# In[1]:


#find all duplicate characters present in the string without using recursion
def dup_char(string1):
    #string1='aabbcc cdeefggh'
    list1=list(string1)
    print(list1)
    set1=set(list1)
    print(set1)
    list2=list(set1)
    print(list2)
    list3=[]
    for i in list2:
        if string1.count(i)>1:
            list3.append(i)
    print("duplicate characters present in the string are:",list3)
    #string1=input("enter the string here:")
    #return dup_char(string1)
string1=input("enter the string here:")
print(dup_char(string1))


# In[2]:


#duplicate characters in a string with recursion
def dup_char(string1):
    #string1='aabbcc cdeefggh'
    list1=list(string1)
    print(list1)
    set1=set(list1)
    print(set1)
    list2=list(set1)
    print(list2)
    list3=[]
    for i in list2:
        if string1.count(i)>1:
            list3.append(i)
    print("duplicate characters present in the string are:",list3)
    x=int(input("enter a value of x 0 or 1:"))
    if x==1:#if x is 1,ask for another string otherwise return
        string1=input("enter the string here:")
        return dup_char(string1)
    else:
        return
string1=input("enter the string here:")
print(dup_char(string1))


# In[ ]:





# In[ ]:




