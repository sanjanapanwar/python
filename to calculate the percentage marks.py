#!/usr/bin/env python
# coding: utf-8

# In[6]:


n=int(input('enter the number of students:'))
dict1={}
for i in range(0,n):
    name=input("enter the name of student:")
    phy=float(input("enter the marks in physics:"))
    chem=float(input("enter the marks in chemistry:"))
    math=float(input("enter the marks in maths:"))
    dict1[name]=[phy,chem,math]
c=dict1[input("enter the name whose percentage has to be calculated:")]
sum1=0
for i in c:
    sum1=sum1+i
print(sum1/3)
    


# In[ ]:





# In[ ]:





# In[ ]:




