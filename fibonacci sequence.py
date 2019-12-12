#!/usr/bin/env python
# coding: utf-8

# In[4]:


def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for n in range(1,20):
    print(fib(n))
   
    
 

