#!/usr/bin/env python
# coding: utf-8

# In[17]:


#linear search without recursion
def linear_search(list1,x):
    #list=[12,14,17,19,20,15]
    for i in range(0,len(list1)):
        if x==list1[i]:
            return i
        else:
            pass
print(linear_search([12,14,17,19,20,25],17))


# In[43]:


#binary search with recursion
def binary_search(list1,l,r,x):
    mid=(l+r)//2
    if list1[mid]==x:
        return mid
    elif list1[mid]<x:
        l=mid+1
        return binary_search(list1,l,r,x)
    else:
        r=mid-1
        return binary_search(list1,l,r,x)
list1=[12,14,17,19,20,25]
x=int(input("enter the element to be search:"))
    
print(binary_search(list1,0,len(list1)-1,x))
        


# In[44]:


#binary search without recursion
def binary_search(list1,l,r,x):
    mid=(l+r)//2
    if list1[mid]==x:
        return mid
    elif list1[mid]<x:
        l=mid+1
    else:
        r=mid-1
list1=[12,14,17,19,20,25]
x=int(input("enter the value of element x:"))
binary_search(list1,0,len(list1)-1,x)


# In[48]:


#linear search with recursion
def linear_search(list1,l,r,x):
    if r<l:
        return -1
    if list1[r]==x:
        return r
    if list1[l]==x:
        return l
    return linear_search(list1,l+1,r-1,x)
list1=[10,5,3,6,2,4]
x=int(input("enter the element to be search:"))
print(linear_search(list1,0,len(list1)-1,x))

    


# In[ ]:




