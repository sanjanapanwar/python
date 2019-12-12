#!/usr/bin/env python
# coding: utf-8

# In[1]:


#bubble sort in python
def bubble_sort():
    list1=[2,6,23,67,13,35,7,0,2]
    for i in range(0,len(list1)-1):
        for j in range(i+1,len(list1)):
            if list1[i]>  [j]:
                temp=list1[i]
                list1[i]=list1[j]
                list1[j]=temp
    return list1
print(bubble_sort())


# In[8]:


#insertion sort in python
def insertion_sort(list1):
    for i in range(1,len(list1)):
        temp=list1[i]
        j=i-1
        while (j>=0 and temp<list1[j]):
            list1[j+1]=list1[j]
            j=j-1
            list1[j+1]=temp
    return list1
list1=[5,1,3,9,8,7,2]
print(insertion_sort(list1))


# In[5]:


#selection sort in python
def selection_sort(list1):
    for i in range(0,len(list1)):
        min_indx=i
        for j in range(i+1,len(list1)):
            if list1[min_indx]>list1[j]:
                min_indx=j
        list1[i],list1[min_indx]=list1[min_indx],list1[i]
    return list1
print(selection_sort([6,3,5,8,2,0,1]))


# In[ ]:




