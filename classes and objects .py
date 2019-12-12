#!/usr/bin/env python
# coding: utf-8

# In[1]:


class complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
x=complex(3.0,4.0)
print("the real part is:",x.r)
print("the imaginary part is:",x.i)


# In[2]:


class dog:
    kind="canine"              #class variable
    def __init__(self,name):   #constructer-called when the object of the class is being created
        self.name=name      #instance variable, #self stored the object of the class
print(dog.kind)                #class variable can be accessed using the name of the class
d=dog('fido')                  #object instantiation
print(d.kind)
print(d.name)
e=dog('buddy')
print(e.kind)
print(e.name)


# In[5]:


#program to count the number of objects
class count:
    count1=0
    def __init__(self):
        count.count1=count.count1+1
        print("the number of objects created :",count.count1)
x=count()
y=count()
z=count()


# In[7]:


class dog:
    list1=[]     
    def __init__(self,name):
        self.name=name
    def add_alist(self,alist):
        self.list1.append(alist)
d=dog('fido')
print(d.name)
e=dog('buddy')
print(e.name)
d.add_alist('roll over')
e.add_alist('play dead')
print(d.list1)


# In[11]:


class dog:
    def __init__(self,name):
        self.name=name
        self.list1=[]
    def add_list(self,alist):
        self.list1.append(alist)
d=dog('fido')
print(d.name)
e=dog('buddy')
print(e.name)
d.add_list('sanjana')
e.add_list('panwar')
print(d.list1)
print(e.list1)

    


# In[12]:


class employee:
    def __init__(self,first,last,sal):
        self.fname=first
        self.lname=last
        self.sal=sal
        self.email=first+'.'+last+'@company.com'
emp1=employee('aayushi','johari',350000)
emp2=employee('test','test',100000)
print("email of employee 1:",emp1.email)
print("email of employee 2:",emp2.email)


# In[13]:


class employee:
    def __init__(self,first,last,sal):
        self.fname=first
        self.lname=last
        self.sal=sal
        self.email=first+'.'+last+'@company.com'
    def fullname(self):
        return '{}{}'.format(self.fname,self.lname)
emp1=employee('aayushi','johari',350000)
emp2=employee('test','test',100000)
print(emp1.email)
print(emp2.email)
print(emp1.fullname())
print(emp2.fullname())


# In[15]:


class employee:
    perc_raise=1.05
    def __init__(self,first,last,sal):
        self.fname=first
        self.lname=last
        self.sal=sal
        self.email=first+'.'+last+'@company.com'
    def fullname(self):
        return '{}{}'.format(self.fname,self.lname)
    def apply_raise(self):
        self.sal=int(self.sal*1.05)
emp1=employee('aayushi','johari',350000)
emp2=employee('test','test',100000)

print("employee 1 initial salary:",emp1.sal)
emp1.apply_raise()
print("employee 1 salary after raise:")
print(emp1.sal)
print("employee 2 initial salary:",emp2.sal)
emp2.apply_raise()
print("employee 2 salary after raise:",emp2.sal)

    


# In[22]:


#assuming that an eamil addresses is of the form 'username@company.com' format,wap to print the username and company name of 
#a given email address
email='sanjanapanwar@gmail.com'
l1=email.split('@')
#print(l1)
username=l1[0]
print('username:',username)
company_com=l1[1]
#print(company_com)
l2=company_com.split('.')
#print(l2)
print("company:",l2[0])


# In[24]:


#inheritance in python:
class employee:
    num_employee=0
    raise_amount=1.04
    def __init__(self,first,last,sal):
        self.first=first
        self.last=last
        self.sal=sal
        self.email=first+'.'+last+'@company.com'
        employee.num_employee+=1
        print("number of employee:",employee.num_employee)
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    def apply_raise():
        self.sal=int(self.sal*raise_amount)
class developer(employee):
    pass
emp1=developer('aayushi','johari',1000000)
print(emp1.email)
        


# In[26]:


class employee:
    num_employee=0
    raise_amount=1.04
    def __init__(self,first,last,sal):
        self.first=first
        self.last=last
        self.sal=sal
        self.email=first+'.'+last+'@company.com'
        employee.num_employee+=1
        print("number of employee:",employee.num_employee)
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    def apply_raise():
        self.sal=int(self.sal*raise_amount)
class developer(employee):
    raise_amount=1.10
emp1=developer('aayushi','johari',1000000)
print(emp1.email)
print(emp1.raise_amount)
emp2=employee('sanjana','panwar',1000000)
print(emp2.raise_amount)
        


# In[29]:


#polymorphism example:
class animal:
    def __init__(self,name):
        self.name=name
        def talk(self):
            pass
class dog(animal):
    def talk(self):
        print("woof!!")
class cat(animal):
    def talk(self):
        print("meow!!")
c=cat('kitty')
c.talk()
d=dog(animal)
d.talk()
        


# In[31]:


class employee:
    num_employee=0
    raise_amount=1.04
    def __init__(self,first,last,sal):
        self.first=first
        self.last=last
        self.sal=sal
        self.email=first+'.'+last+'@company.com'
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    def apply_raise():
        self.sal=int(self.sal*raise_amount)
class developer(employee):
    raise_amount=1.10
    def __init__(self,first,last,sal,prog_lang):
        super().__init__(first,last,sal)
        self.prog_lang=prog_lang
emp1=developer('aayushi','johari',1000000,'python')
print(emp1.prog_lang)
print(emp1.sal)


# In[34]:


class employee:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empcount+=1
    def displaycount(self):
        print("total employee:",employee.empcount)
    def displayemployee(self):
        print("name=",self.name)
        print("salary:",self.salary)
emp1=employee('zara',2000)
emp2=employee('manni',5000)
print("emp 1 info:")
emp1.displayemployee()
print("emp 2 info:")
emp2.displayemployee()
print("total employee:",employee.empcount)

        


# In[35]:


#deleting objects in python
#destructer:__del()__
class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"destroyed")
pt1=point()
pt2=pt1
pt3=pt1
print(id(pt1),id(pt2),id(pt3))
del pt1
del pt2
del pt3


# In[39]:


class parent:
    parentattr=100
    def __init__(self):
        print("calling parent constructer")
    def parentmethod(self):
        print("calling parent method")
    def setAttr(self,attr):
        parent.parentattr=attr
    def getAttr(self):
        print("parent attribute:",parent.parentattr)
class child(parent):
    def __init__(self):
        print("calling child constructer")
    def childmethod(self):
        print("calling child method")
c=child()
c.childmethod()
c.parentmethod()
c.setAttr(200)
c.getAttr()


# In[40]:


#private variables:
class justcounter:
    __secretcount=0
    def count(self):
        self.__secretcount+=1
        print(self.__secretcount)
counter=justcounter()
counter.count()
counter.count()
print(counter.__secretcount)


# In[45]:


#python static method
class maths:
    def add(x,y):
        return x+y
maths.add=staticmethod(maths.add)
print("the sum is:",maths.add(5,10))
#topics left:-operator overloading,abstraction,regular expressions,property decorators


# In[1]:


#python lambda function
g=lambda x:x*x*x
print(g(7))


# In[3]:


#lambda() function with filter()
#the filter function takes in a function and a list as arguments
li=[5,7,22,97,54,62,77,23,73,61]
final_list=list(filter(lambda x:(x%2!=0),li))
print(final_list)


# In[8]:


#lambda function with map
#the map() function in python takes in a function and a list as argument
li=[5,7,22,97,54,62,77,23,73,61]
final_list=list(map((lambda x:x*2),li))
print(final_list)


# In[11]:


#lambda function with reduce
#the reduce function in python takes in a function and a list as argument
from functools import reduce
li=[5,8,10,20,50,100]
sum=reduce((lambda x,y:x+y),li)
print(sum)


# In[14]:


#decorators in python
def first(msg):
    print(msg)
first("hello")
second=first
second("hey")


# In[15]:


def first(msg):
    print(msg)
first("hello")
second=first
second("hey")
first("Hello")


# In[23]:


#function passed as argument
def inc(x):
    return x+1
def dec(x):
    return x-1
def operate(func,x):
    result=func(x)
    return result
print(operate(inc,3))
print(operate(dec,4))


# In[24]:


def sum(x,y):
    return x+y
def res(func,x,y):
    out=func(x,y)
    return out
print(res(sum,3,4))


# In[31]:


#a function can return another function
def is_called():
    def is_returned():
        print("hello")
    return is_returned()

is_called()


# In[32]:


#nested function
def transmit_to_space(message):
    def data_transmitter():
        print(message)
    return data_transmitter()
print(transmit_to_space("hello sanjana"))


# In[34]:


def print_msg(msg):
    def printer():
        print(msg)
    return printer()
print(print_msg("hey"))


# In[37]:


def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
    return inner
def ordinary():
    print("i am ordinary")
ordinary()
pretty=make_pretty(ordinary)
pretty()


# In[41]:


def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
    return inner
def ordinary():
    print("i am ordinary")
ordinary()
print(make_pretty(ordinary()))


# In[42]:


@make_pretty
def ordinary():
    print("i am ordinary")
#this is equivalent to


# In[44]:


#to this
def ordinary():
    print("i am ordinary")
ordinary=make_pretty(ordinary)


# In[48]:


def smart_divide(func):
    def inner(a,b):
        print("i am going to divide ",a,"and",b)
        if b==0:
            print("whoops!cannot divide")
            return
        return func(a,b)
    return inner
@smart_divide
def divide(a,b):
    return a/b
print(divide(2,5))
print(divide(2,0))


# In[49]:


#chaining decoraters in python
def star(func):
    def inner(*args,**kwargs):
        print("*"*30)
        func(*args,**kwargs)
        print("*"*30)
    return inner
def percent(func):
    def inner(*args,**kwargs):
        print("%"*30)
        func(*args,**kwargs)
        print("%"*30)
    return inner
@star
@percent
def printer(msg):
    print(msg)
printer("hello")
    


# In[50]:


#property decorators
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.gotmarks=self.name+'obtained'+self.marks+'marks'
st=student('jaki','25')
print(st.name)
print(st.marks)
print(st.gotmarks)


# In[51]:


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.gotmarks=self.name+'obtained'+self.marks+'marks'
st=student('jaki','25')
print(st.name)
print(st.marks)
print(st.gotmarks)

st.name='anusha'
print(st.name)
print(st.gotmarks)


# In[52]:


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        #self.gotmarks=self.name+'obtained'+self.marks+'marks'
    def gotmarks(self):
        return self.name+'obtained'+self.marks+'marks'
        

st=student('jaki','25')
print(st.name)
print(st.marks)
print(st.gotmarks())
st.name='anusha'
print(st.name)
print(st.gotmarks())


# In[53]:





# In[ ]:




