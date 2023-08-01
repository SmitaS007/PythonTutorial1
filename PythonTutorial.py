#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("This is Smita")


# In[2]:


get_ipython().run_line_magic('whos', '')


# In[3]:


x=45


# In[4]:


x


# In[5]:


print(type(x))


# In[6]:


get_ipython().run_line_magic('whos', '')


# In[7]:


student="Sam"


# In[8]:


student


# In[9]:


student="Matt"


# In[10]:


student


# In[11]:


student='Matt'


# In[12]:


student


# In[13]:


student='bob'


# In[14]:


student


# In[15]:


student=1,3,45,5


# In[16]:


student


# In[17]:


get_ipython().run_line_magic('whos', '')


# In[19]:


type(student)


# In[20]:


a1=10
a1


# In[21]:


type(a1)


# In[24]:


a1=3.455
a1
type(a1)


# In[26]:


a1= True
type(a1)


# In[27]:


a1="Hello"
type(a1)


# In[28]:


a1=3+4j
type(a1)


# In[30]:


#Arethmetic Operation


# In[32]:


a=10
b=20


# In[33]:


a,b


# In[34]:


a+b


# In[35]:


a-b


# In[36]:


a*b


# In[37]:


a/b


# In[38]:


a%b


# In[39]:





# asdfg
# 

# # use markdown
# $a=b+c

# $a=b+c

# $a=b+c
# 

# In[40]:


#Relational Operators


# In[41]:


#<,>,==,!=


# In[42]:


a=50
b=100


# In[43]:


a>b


# In[44]:


a<b


# In[45]:


a==b


# In[46]:


a!=b


# In[47]:


_


# In[48]:


#Logical Operators


# In[ ]:


& , |


# In[49]:


a=True
b=False


# In[50]:


a and b


# In[51]:


a or b


# In[52]:


a and a


# In[53]:


b and b


# In[54]:


a or a


# In[55]:


b or b


# In[56]:


a & a


# In[57]:


a|a


# In[58]:


a|b


# In[59]:


str1='This is my first string'


# In[60]:


str1


# In[61]:


str2="This is my sencond string"


# In[62]:


str2


# In[63]:


str3='''
This string has
lot of
lines
'''


# In[64]:


str3


# In[65]:


str4='This is my string This is my string This is my string This is my string This is my string This is my stringThis is my string This is my stringThis is my stringThis is my string This is my stringThis is my string This is my stringThis is my stringThis is my stringThis is my stringThis is my stringThis is my string'


# In[66]:


str4


# In[67]:


my_string="My name is Smita"


# In[69]:


my_string[0]


# In[70]:


my_string[-5]


# In[74]:


my_string[1:7]


# In[78]:


my_string[-1:-3] #does not work


# In[79]:


my_string[6:10] #includes spaces and starts with 0


# In[80]:


my_string[10]


# In[81]:


len(my_string)


# In[82]:


my_string.lower()


# In[84]:


my_string.upper()


# In[87]:


my_string.replace('Smita','Maau')


# In[90]:


my_string.replace('a','u')


# In[91]:


my_string.count("My")


# In[92]:


my_string.find("Smita")


# In[93]:


my_string.find("i")


# In[94]:


str00="President obama is the best precident of united states"


# In[95]:


str00


# In[96]:


str00.split('e')


# In[97]:


tup1=(1,True,2.4, 5-7j,'dffg')


# In[98]:


tup1


# In[99]:


type(tup1)


# In[100]:


tup1[0]


# In[101]:


tup1[-2]


# In[104]:


tup1[1:3]


# In[106]:


tup1[2]='dfvg'


# In[107]:


len(tup1)


# In[108]:


tup2=4,5,6


# In[109]:


tup2


# In[110]:


type(tup2)


# In[112]:


tup1+tup2


# In[113]:


tup2+tup1


# In[114]:


tup1*5


# In[117]:


tup2*2+tup1


# In[119]:


tup2*4+tup1*2


# In[121]:


min(tup2)


# In[122]:


max(tup2)


# In[123]:


#List in Python


# In[124]:


#List is mutible and tuple is inmutable


# In[125]:


l1=[1,'sparta',3.45,True]


# In[126]:


l1


# In[127]:


l1[1]


# In[130]:


l1[2:4]


# In[131]:


l1[-1]


# In[132]:


l1[0]=400


# In[133]:


l1


# In[137]:


l1.append(-87.99)


# In[138]:


l1


# In[139]:


l1.pop()


# In[140]:


l1


# In[141]:


l1.pop()


# In[142]:


l1


# In[143]:


l1.reverse()


# In[144]:


l1


# In[145]:


l1.insert(0,'Hello')


# In[146]:


l1


# In[147]:


l1.insert(-2,45.5)


# In[148]:


l1


# In[154]:


l1=["d","a","r","z","y"]


# In[155]:


l1


# In[157]:


l1.sort()


# In[158]:


l1


# In[159]:


l2=["apple","Banana","Mango"]


# In[160]:


l2


# In[161]:


l1+l2


# In[162]:


l2+l1


# In[163]:


l2*5+l1


# In[1]:


#Dictionary
#Dictionary is mutable


# In[5]:


d1={'Apple':50,'Mango':100,'Guava':200,'Banana':500}


# In[6]:


type(d1)


# In[7]:


d1.keys()


# In[8]:


d1.values()


# In[9]:


d1["Orange"]=40


# In[10]:


d1


# In[11]:


d1["Banana"]=30


# In[12]:


d1


# In[17]:


d2={"Grapes":300, "Pomogranate":600, "Watermelon":400}


# In[18]:


d2


# In[19]:


d1.update(d2)


# In[20]:


d1


# In[22]:


d1.pop("Banana")


# In[23]:


d1


# In[24]:


#Sets in python


# In[25]:


s1={1,2.445,"sparta"}


# In[26]:


type(s1)


# In[27]:


s1={1,2.445,"sparta","sparta"}
#Duplicates are not allowed in sets


# In[28]:


s1


# In[29]:


s1.add(False)


# In[30]:


s1


# In[31]:


s1.update(["hello",2345,5+7j])


# In[32]:


s1


# In[33]:


s1.remove(2345)


# In[34]:


s1


# In[35]:


s1.remove("hello")


# In[36]:


s1


# In[37]:


s2={1,23,4,5,5}


# In[38]:


s2


# In[39]:


s1.union(s2)


# In[41]:


s1.intersection(s2)


# In[42]:


#If Statement


# In[43]:


a=10
b=20


# In[46]:


if(b>a):
    print("b is greater than a")
else:
    print("b is smaller than a")


# In[48]:


if(a==b):
    print("a and b are same")
else:
    print("a and b are not same")


# In[49]:


c=30


# In[50]:


if(a>b) & (a>c):
    print("a is greater")
elif(b>a) & (b>c):
    print("b is greater")
else:
    print("c is greater")


# In[51]:


#if with tuple


# In[52]:


tup1=("a","b","c")


# In[53]:


if 'a' in tup1:
    print("Value is present")


# In[54]:


if 'z' in tup1:
    print("Value is present")
else:
    print("Value is not present")


# In[60]:


l1=['a','b','c']


# In[61]:


if l1[1]=='b':
    l1[1]='z'


# In[62]:


l1


# In[86]:


d1={"k1":10,"k2":20,"k3":30}


# In[87]:


d1


# In[88]:


if d1["k3"]==30:
    d1["k3"]=d1["k3"]+100


# In[89]:


d1


# In[90]:


#Looping statements


# In[91]:


i=1
while i<=10:
    print(i)
    i=i+1


# In[92]:


i=1
n=2
while i<=10:
    print(n," ", i, " ", n*i)
    i=i+1


# In[93]:


#whilw with list


# In[94]:


l1=[1,2,3,4,5]


# In[95]:


i=0


# In[96]:


while i<len(l1):
    l1[i]=l1[i]+100
    i=i+1


# In[97]:


l1


# In[98]:


#For Loop


# In[99]:


l1=["Mango","Apple","Orange","Grapes"]


# In[100]:


for i in l1:
    print(i)


# In[101]:


l1=["Orange","Black","White"]
l2=["Chair","Book","Laptop"]


# In[102]:


for i in l1:
    for j in l2:
        print(i, j)


# In[1]:


#Functions


# In[2]:


def hello():
    print("Hello World")


# In[3]:


hello()


# In[4]:


def add_10(x):
    return x+10


# In[5]:


add_10(4)


# In[11]:


def add1(f):
    print(f+1)


# In[12]:


add1(7)


# In[13]:


def check(x):
    if x%2==0:
        print("X is even")
    else:
        print("X is odd")
    


# In[14]:


check(5)


# In[15]:


check(4)


# In[16]:


g=lambda x:x*x*x


# In[18]:


g(7)


# In[19]:


#Lambda with filter


# In[24]:


l1=[1,3,3,2,4,63,5646,7784,3234,646,24,5,245,256,73,226,6]
l2=list(filter(lambda x: (x%2!=0),l1))


# In[25]:


l2


# In[26]:


#Lambda with map


# In[27]:


l1=[1,2,3,4,5,6,7,8]


# In[28]:


list(map(lambda x:(x*2),l1))


# In[29]:


#Lambda with reduce


# In[30]:


from functools import reduce


# In[32]:


sum=(reduce(lambda y,z: (y+z),l1))


# In[33]:


sum


# In[36]:


l1


# In[47]:


class Phone:      #Name of a class starts with capital letter
    def make_call(self):
        print("Making phone call")
    
    def play_game(self):
        print("Playing game")
    


# In[48]:


Phone()


# In[49]:


P1=Phone()


# In[50]:


P1


# In[51]:


P1.make_call()


# In[52]:


P1.play_game()


# In[57]:


class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("Making phone call")
    def play_game(self):
        print("Playing game")
        


# In[58]:


p2=Phone()


# In[59]:


p2.set_color("Blue")


# In[60]:


p2.set_cost(10000)


# In[62]:


p2.show_color()


# In[63]:


p2.show_cost()


# In[64]:


#Creating a class with constructer


# In[65]:


class Employee:
    def __init__(self, name, age, salary, gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def show_employee_details(self):
        print("name of employee is",self.name)
        print("age of employee is", self.age)
        print("salary of employee is", self.salary)
        print("gender of employee is", self.gender)
        


# In[68]:


e1=Employee("Smita", 30,200000,"Female")


# In[69]:


e1.show_employee_details()


# In[70]:


#one more example of class


# In[71]:


class cricket:
    def __init__ (self,name, score, wicket, age, stadium):
        self.name=name
        self.score=score
        self.wicket=wicket
        self.age=age
        self.stadium=stadium
    
    def show_records(self):
        print("Name of player",self.name)
        print("Runs scored by the", self.name, self.score)
        print("Wickets by", self.name, self.wicket)
        print("Age of the player", self.age)
        print("Name of the stadium", self.stadium)


# In[73]:


c1=cricket("Snehalkumar", 100, 10,30,"Pune")


# In[74]:


c1.show_records()


# In[ ]:


#inheritance


# In[ ]:


#Create base/super class


# In[76]:


class vehicle:
    def __init__(self, mileage, cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("Mileage of vehicle is",self.mileage)
        print("Cost of vehicle is", self.cost)
        print("I am a vehicle")
        


# In[78]:


v1=vehicle(100,10000)


# In[79]:


v1.show_details()


# In[81]:


class car(vehicle):
    def show_car_details(self):
        print("I am a car")


# In[83]:


c1=car(244,2345)


# In[84]:


c1.show_car_details()


# In[85]:


c1.show_details()


# In[86]:


#Child class with constructer


# In[90]:


class car(vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp
        
    def show_car_details(self):
        print("Number of tyres in car",self.tyres)
        print("HP of car is", self.hp)
        print("I am a car")


# In[91]:


c1=car(100,1999,4,123456789)


# In[92]:


c1.show_car_details()


# In[93]:


c1.show_details()


# In[94]:


#Multiple inheritance


# In[109]:


class Parent1:
    def assign_string_one(self,str1):
        self.str1=str1
    def show_string_one(self):
        return self.str1


# In[110]:


class Parent2:
    def assign_string_two(self,str2):
        self.str2=str2
    def show_string_two(self):
        return self.str2


# In[111]:


class Child(Parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3=str3
        
    def show_string_three(self):
        return self.str3


# In[112]:


my_child=Child()


# In[113]:


my_child.assign_string_one("I am a string of parent1")


# In[114]:


my_child.assign_string_two("I am a string of parent2")


# In[115]:


my_child.assign_string_three("I am a string of child")


# In[116]:


my_child.show_string_one()


# In[117]:


my_child.show_string_two()


# In[118]:


my_child.show_string_three()


# In[119]:


#Multi Level Inheritance


# In[122]:


class Parent:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        return self.name


# In[123]:


class Child(Parent):
    def get_age(self,age):
        self.age=age
    def show_age(self):
        return self.age


# In[124]:


class GrandChild(Child):
    def get_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        return self.gender


# In[125]:


gc=GrandChild()


# In[126]:


gc.get_name("Smita")


# In[127]:


gc.get_age(30)


# In[128]:


gc.get_gender("Female")


# In[129]:


gc.show_name()


# In[130]:


gc.show_age()


# In[131]:


gc.show_gender()


# In[132]:


#Libraries in Python


# In[134]:


#Python NumPy


# In[1]:


get_ipython().run_line_magic('pinfo', 'Numpy')


# In[2]:


import numpy as np


# In[7]:


l1=np.array([1,2,3,4,5,6])


# In[9]:


l1


# In[10]:


l1=[1,2,3,4,5]


# In[11]:


n1=np.array(l1)


# In[12]:


n1


# In[13]:


type(n1)


# In[14]:


n2=np.array([[1,2,3,4,5],[1,2,3,4,5]])


# In[15]:


n2


# In[16]:


type(n2)


# In[18]:


n3=np.zeros((5,5))


# In[19]:


n3


# In[20]:


n4=np.zeros((1,2))


# In[21]:


n4


# In[28]:


n5=np.full((5,10),5)


# In[29]:


n5


# In[30]:


n6=np.arange(10,20)


# In[31]:


n6


# In[37]:


n6=np.arange(6,22)


# In[38]:


n6


# In[39]:


n7=np.arange(4,5678,100)


# In[40]:


n7


# In[42]:


n8=np.random.randint(56,100,10)


# In[43]:


n8


# In[52]:


n9=np.array([[12,3,4,5,66,76],[234,35,5,5,5,5]])


# In[53]:


n9


# In[56]:


n9.shape=(6,2)


# In[57]:


n9


# In[58]:


n9.shape=(12,1)


# In[59]:


n9


# In[60]:


n10=np.array([1,2,3,4])
n11=np.array([5,6,7,8])


# In[63]:


np.vstack((n10,n11))             #Vertically Stack array


# In[64]:


np.hstack((n10,n11))             #Horizontal Stacking of array


# In[66]:


np.column_stack((n10,n11))       #Column Stack array


# In[67]:


#NumPy Intersection and Difference


# In[68]:


import numpy as np


# In[69]:


n12=np.arange(10,20)


# In[70]:


n12


# In[74]:


n13=np.arange(15,30)


# In[75]:


n13


# In[76]:


np.intersect1d(n12,n13)


# In[77]:


np.setdiff1d(n12,n13)     #Order of n12 and n13 matters


# In[78]:


np.setdiff1d(n13,n12)          #Order of n12 and n13 matters


# In[79]:


#Numpy array mathematics


# In[82]:


np.sum([n10,n11])


# In[83]:


np.sum([n12,n13])


# In[84]:


np.sum([n10,n11], axis=0)  #Row Sum


# In[85]:


np.sum([n10,n11], axis=1)  #Column Sum


# In[86]:


#Basic Addition


# In[87]:


n10


# In[88]:


n10=n10+1


# In[89]:


n10


# In[90]:


#Basic Substraction


# In[91]:


n10=n10-1


# In[92]:


n10


# In[93]:


#Basic Multiplication


# In[94]:


n10=n10*2


# In[95]:


n10


# In[96]:


#Basic Division


# In[97]:


n10=n10/2


# In[98]:


n10


# In[99]:


#Mean


# In[106]:


n14=np.array([1,24,4,5,7,73,7,6])


# In[107]:


n14


# In[108]:


np.mean(n14)


# In[101]:


#Median


# In[109]:


np.median(n14)


# In[110]:


#Standard deviation


# In[111]:


np.std(n14)


# In[112]:


#Numpy save & load


# In[113]:


import numpy as np
n15=np.array([12,13,13,13,14,54,5])
np.save("Myarray",n15)


# In[114]:


newn15=np.load("Myarray.npy")


# In[115]:


newn15


# In[2]:


##Pandas Data Manipulation


# In[3]:


import pandas as pd


# In[4]:


#Series object---One dimensional


# In[7]:


s1=pd.Series([1,2,3,4,5]) # S is capital in series


# In[8]:


s1


# In[9]:


type(s1)


# In[10]:


import pandas as pd


# In[12]:


s2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])


# In[13]:


s2


# In[14]:


type(s2)


# In[17]:


s3=pd.Series({'k1':10,'k2':20,'k3':30})


# In[18]:


type(s3)


# In[19]:


s3


# In[21]:


import pandas as pd
s4=pd.Series({'k1':2,'k2':45,'k3':23},index=['k3','k2','k1','k4'])


# In[22]:


s4


# In[23]:


l1=[1,2,3,4,5,6,7,8,9]


# In[25]:


s1=pd.Series(l1)


# In[26]:


s1


# In[27]:


s1[4]


# In[29]:


s1[:5]


# In[30]:


s1[:-5]


# In[32]:


s1+5         #Sum


# In[33]:


s1-5              #Substraction


# In[35]:


s1*23              #Multiplication


# In[36]:


s1/5            #Division


# In[38]:


s2=pd.Series([10,20,30,40,50,60,70,80,90])


# In[39]:


s2


# In[40]:


s1+s2


# In[41]:


s1-s2


# In[42]:


s1*s2


# In[43]:


s1/s2


# In[44]:


###Mulitdiminsional Data Structure


# In[47]:


import pandas as pd

pd.DataFrame({"Name":['Smita','Snehal','Shubham'],"Marks":[345,365,383]})


# In[56]:


iris=pd.read_csv("D:\Prepration\Python\Iris.csv")


# In[57]:


iris


# In[60]:


iris.head()


# In[61]:


iris.tail()


# In[62]:


iris.shape


# In[63]:


iris.describe()


# In[64]:


iris.iloc[0:3,0:2]


# In[67]:


iris.iloc[5:11,1:4]


# In[72]:


iris.loc[1:10,("PetalLengthCm","Species")]


# In[73]:


iris.drop('SepalLengthCm',axis=1)     #Axis=1 meaning drop the column


# In[80]:


i1=iris.drop([2,3,4],axis=0)      #Axis= 0 Meaning drop row


# In[81]:


i1.head()


# In[82]:


iris.min()


# In[83]:


iris.max()


# In[84]:


iris.mean()


# In[85]:


iris.median()


# In[86]:


def double_make(s):
    return s*2


# In[88]:


iris[['SepalWidthCm','PetalWidthCm']].apply(double_make)


# In[91]:


iris['Species'].value_counts()


# In[92]:


iris.sort_values(by="PetalWidthCm")


# In[1]:


#Pandas Revision


# In[2]:


#Series is one dimensional


# In[3]:


import pandas as pd


# In[4]:


s1=pd.Series([1,2,3,4,5])


# In[5]:


s1


# In[6]:


type(s1)


# In[7]:





# In[8]:


import numpy as np


# In[10]:


v=np.random.randint(20,30)


# In[11]:


type(v)


# In[12]:


v


# In[24]:


A=np.random.rand(1000)


# In[25]:


A


# In[26]:


type(A)


# In[27]:


import matplotlib.pyplot as plt


# In[29]:


plt.hist(A,bins=100)


# In[30]:


B=np.random.randn(100000)


# In[31]:


plt.hist(B,bins=200)


# In[32]:


C=np.random.rand(2,3)


# In[33]:


C


# In[34]:


C.ndim


# In[35]:


C=np.random.rand(2,3,4,2)


# In[36]:


C


# In[37]:


C.ndim


# In[39]:


D=np.arange(100).reshape(4,25)


# In[40]:


D.shape


# In[41]:


D


# In[42]:


D=np.arange(100).reshape(4,5,5)


# In[43]:


D


# In[44]:


D.shape


# In[48]:


get_ipython().run_line_magic('pinfo', 'np.zeros')


# In[49]:


#Numpy Slicing


# In[50]:


A=np.arange(100)


# In[51]:


A


# In[52]:


b=A[3:10]
print(b)


# In[53]:


b[0]=-1200


# In[54]:


b


# In[55]:


A


# In[57]:


b=A[3:10].copy()


# In[58]:


b


# In[59]:


A[::5]


# In[60]:


A[::-5]


# In[61]:


A[::-1]


# In[62]:


get_ipython().run_line_magic('pinfo', 'np.indices')


# In[66]:


B=(A==-1200)*np.arange(A.size)


# In[67]:


B


# In[68]:


A.indices(-1200)


# In[69]:


idx=np.argwhere(A==-1200)[0][0]


# In[70]:


idx


# In[71]:


A[idx]=3


# In[72]:


A


# In[78]:


A=np.round(10*np.random.rand(5,4))


# In[79]:


A


# In[ ]:


a[1,2]

