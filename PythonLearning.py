#!/usr/bin/env python
# coding: utf-8

# This is our first programm in Python.

# In[1]:


print("Hello World")


# In[2]:


print('Hello World')


# $a=b+c
# 

# $a=b+c$

# In[3]:


a,b=4,5.0


# In[4]:


a


# In[5]:


b


# In[6]:


del a


# In[7]:


a


# In[8]:


x = 2


# In[9]:


x


# # Variables
# 

# In[10]:


x=3


# In[11]:


get_ipython().run_line_magic('Whoes', '')


# In[12]:


get_ipython().run_line_magic('Whos', '')


# In[13]:


get_ipython().run_line_magic('Whos', '')


# In[ ]:





# In[14]:


print(type(x))


# In[15]:


x=5.7


# In[16]:


get_ipython().run_line_magic('whos', '')


# In[17]:


print(type(x))


# In[18]:


get_ipython().run_line_magic('whos', '')


# In[19]:


abcd=556.32


# In[20]:


get_ipython().run_line_magic('whos', '')


# In[21]:


a,b,c,d,e=3,6.0,5,-5,7.2


# In[22]:


get_ipython().run_line_magic('whos', '')


# In[23]:


del d


# In[24]:


get_ipython().run_line_magic('whos', '')


# In[25]:


print(d)


# In[26]:


c=2+4j


# In[27]:


print(type(c))


# In[28]:


get_ipython().run_line_magic('whos', '')


# In[29]:


b=5.7-2j


# In[30]:


print(type(b))


# In[31]:


s="My name is smita"


# In[32]:


print(type(s))


# In[33]:


s=smita


# # Operators

# In[34]:


sumofAandB=a+c


# In[35]:


sumofAandB


# In[36]:


print(type(sumofAandB))


# In[37]:


a


# In[38]:


c


# In[39]:


type(a+b)


# In[40]:


print(((a+b)**3)/6)


# In[41]:


s1="hello"
s2="world"
s=s1+s2
print(s)


# In[42]:


_


# In[43]:


3/5


# In[44]:


_


# In[45]:


_=6


# In[46]:


_


# In[47]:


3w=6


# In[48]:


6+9


# In[49]:


_w=98


# In[50]:


_d=98


# In[51]:


_d


# # Type Bool and Comparisions

# In[46]:


a=True
b=True
c=False


# In[52]:


get_ipython().run_line_magic('whos', '')


# In[74]:


print(a and b)


# In[75]:


print(a and c)


# In[76]:


print(b and c)


# In[77]:


d=a or c
print(d)


# In[78]:


type(d)


# In[79]:


not(a)


# In[80]:


not(b)


# In[81]:


not(c)


# # Comparsions

# In[82]:


print(2<4)


# In[83]:


c=2<3


# In[84]:


c


# In[85]:


type(c)


# In[86]:


print(type(c))


# In[87]:


print(c)


# In[88]:


3==4


# In[89]:


d = 3==4


# In[90]:


print(d)


# In[91]:


3==3.0 


# In[92]:


x=4
y=9
z=8.3
r=-3


# In[93]:


(x<y) and (z<y) or (r==x)


# In[94]:


(x<y) and (r==x) or (z>y)


# In[95]:


(r==x) and x


# In[96]:


4 or 5


# In[97]:


5 or 4


# In[98]:


round(5.4)


# In[99]:


round(4.65442)


# In[100]:


round(4.442)


# In[101]:


print("A")


# In[102]:


print(round(4.68765,3))


# In[103]:


print(round(5.24567))


# In[104]:


divmod(27,6)


# In[105]:


get_ipython().run_line_magic('pinfo', 'divmod')


# In[106]:


divmod(34,5)


# In[107]:


G=divmod(78,998)


# In[108]:


G


# In[109]:


type(G)


# In[110]:


get_ipython().run_line_magic('pinfo', 'tuple')


# In[111]:


G[0]


# In[112]:


G[1]


# In[113]:


divmod(34,556)[0]


# In[114]:


divmod(34,5)[0]


# In[115]:


print(isinstance(1,int))


# In[116]:


print(isinstance(1,float))


# In[117]:


isinstance(1,int)


# In[118]:


isinstance(2+4j,(int,float,str))


# In[119]:


pow(2,4)


# In[120]:


pow(2,3,4)


# In[121]:


pow(2,3,5)


# a=d/g+r*d-h

# In[122]:


input("Enter Something")


# In[123]:


input("Enter your full name")


# In[124]:


input(4)


# In[125]:


x=input("Enter a number")


# In[126]:


type(x)


# In[127]:


x


# In[128]:


x=int(x)


# In[129]:


x


# In[130]:


type(x)


# In[131]:


print(x-2)


# In[132]:


type((x-3))


# In[133]:


a=float(input("Enter a real number:"))


# In[134]:


a


# In[135]:


type(a)


# In[136]:


a=float(input("Enter a real number:"))


# In[137]:


a


# In[138]:


a=float(input("Enter a real number:"))


# # Control Flow

# In[139]:


a=int(input())
b=int(input())
if a>b:
    print(a)
    print("I am still inside if condition")
print("I am ouside if condition")


# In[140]:


a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
if a>b:
    print(a)
if b>a:
    print(b)


# In[141]:


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
if a>b:
    print(a)
else:
    print(b)


# In[142]:


a=float(input("Enter value of a:"))
b=int(input("Enter value of b:"))
if a>b:
    print(a)
    print("if part")
else:
    print(b)
    print("else part")


# In[143]:


a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
if a>b:
    print(a)
elif a==b:
    print("a=b")
else:
    print(b)


# In[144]:


a=int(input("Enter Marks:"))
if a>=85:
    print("A+ Grade")
elif ((a>=80) and (a<85)):
    print("A- Grade")
elif ((a<80) and (a>=75)):
    print("B+ Grade")
elif ((a<75) and (a>70)):
    print("B- Gader")
else:
    print("C Grade")


# In[145]:


a=3
if a>10:
    print(">10")
elif not (a>10):
    print("Else part")


# # Nested if

# In[146]:


x=int(input("Enter value of x:"))

if x>10:
    print("X is greater than 10")
    if x>20:
        print("X is also greater than 20")
        if x>30:
            print("X is greater than 30")
        else:
            print("X is smaller than 30")
    else:
        print("X is smaller than 20")
else:
    print("X is smaller that 10")


# In[147]:


#comment 


# In[148]:


x=float(input("Enter a real number:"))


# In[149]:


#comment
"""
multiline comments are difined in three inverted coma
"""
"""
User will enter a floating point number let say 238.915. Your task is to find out the interger portion
before the point (in this case 238) and then check if that inter=ger portion is an even number or not?
"""

x = float(input("Enter a real number: "))
x=round(x)
if (x%2)==0:
    print("x is even number")
else:
    print("x is odd number")


# In[150]:


x=float(input("Enter a real number:"))


# In[151]:


get_ipython().run_line_magic('pinfo', 'input')


# In[152]:


7%2


# # Control Flows(Loops)

# In[153]:


n=int(input("Enter the value of n:"))
i=1
while i<n:
    print(i)
    i=i+1
print("Done")


# In[154]:


n=int(input("Enter the value for n:"))
i=1
while i<=n:
    if type(i*0.5)==int
    print(i*i)
    i=i+1
print("Done")
    


# In[155]:


math.sqrt(4)


# In[156]:


get_ipython().run_line_magic('pinfo', 'sqrt')


# In[157]:


import math


# In[158]:


sqrt(4)


# In[159]:


(type(4*0.5))=int


# In[160]:


type(3)


# In[161]:


type(3)==int


# In[ ]:


n=10
i=1
while True:
    if i%9==0:
        print("inside if")
        break
    else:
        print("inside else")
        
        
        


# # For Loop
# 

# In[ ]:


L=[]


# In[ ]:


L


# In[ ]:


L=[2,3,4]


# In[ ]:


L


# In[ ]:


L=[]
for i in range(10):
    print(i+1)
    L.append(i**2)


# In[ ]:


L


# In[ ]:


L=[]
for i in range(10):
    print(i+1)
    L.append(i)
    


# In[ ]:


L


# In[ ]:


A=[]
for i in range(0,10,2):
    print(i)
    A.append(i*3)
    


# In[ ]:


A


# In[ ]:


B=[]
for i in range(5,500,50):
    print(i,i)
    B.append(i*i)


# In[ ]:


B


# S={"apple",4.9,"Cherry"}
# i=1
# for x in S:
#     print(x)
#     i+=1
#     if i==4:
#         break
#     else:
#         pass
# else:e
#     print('Loop Completes its iterations')
# print("Outside the loop")

# # Control Flow (Exploring a Dictionary)

# In[ ]:


D={"A":44,"B":-19,"C":"abc"}
for x in D:
    print(x,D[x])


# In[ ]:


print(1,2)


# In[ ]:


""" Given a list of numbers i.e. [1,2,4,-5,7,9,3,2], make another list that contains all the items in sorted order 
from min to max i.e your results will be another list like [-5,1,2,3,4,5,7,9]

"""

L=[1,2,4,-5,7,9,3,2]
for j in range(len(L)):
    m=L[j]
    idx=j
    c=j
    for i in range(j,len(L)):
        if L[i]<m:
            m=L[i]
            idx=c
        c+=1
    tmp=L[j]
    L[j]=m
    L[idx]=tmp
print(L)

        

        

        


# # Functions

# In[ ]:


def printSuccess():
    print("The task was sucessful")
    print("Movint to the next task")
    print("Send me the next task")


# In[ ]:


printSuccess()


# # def trial():
#     
#     x=int(input("Enter value of x:"))
# 
#     if x>10:
#     print("X is greater than 10")
#         if x>20:
#             print("X is also greater than 20")
#             if x>30:
#                 print("X is greater than 30")
#             else:
#                 print("X is smaller than 30")
#         else:
#             print("X is smaller than 20")
#     else:
#         print("X is smaller that 10")

# In[ ]:


get_ipython().run_line_magic('pinfo', 'len')


# In[ ]:


get_ipython().run_line_magic('pinfo2', 'len')


# In[ ]:


help(printSuccess)


# In[ ]:


def printMessage(msg):
    """ The function prints the message supplied by the user or prints that msg is not in the form of string"""
    
    if isinstance(msg,str):
        print(msg)
    else:
        print("Your input argument is not a string")
        print("Here is the type of what you heve supplied:",type(msg))
        


# In[ ]:


get_ipython().run_line_magic('pinfo2', 'printMessage')


# In[27]:


printMessage("This is the message")


# In[28]:


printMessage(123)


# In[29]:


get_ipython().run_line_magic('pinfo2', 'isinstance')


# In[31]:


def printMessage(msg):
    """ The function prints the message supplied by the user or prints that msg is not in the form of string"""
    
    if type(msg)==str:
        print(msg)
    else:
        print("Your input argument is not a string")
        print("Here is the type of what you heve supplied:",type(msg))


# In[32]:


printMessage("Thsi is a message")


# In[36]:


printMessage(2345)


# In[37]:


def printMessage(msg1, msg2):
    print(msg1, msg2)


# In[39]:


printMessage(1,2)


# In[45]:


def mypow(a,b):
    """ Thsi function computes power just like builtin pow function"""
    c=a**b
    print(c)


# In[46]:


mypow(3,4)


# In[49]:


def checkargs(a,b,c,d,e):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        print((a+b+c)**2)
    else:
        print("Error: The input arguments are not of the expected types")


# In[51]:


checkargs(3,4,5,5,6)


# In[53]:


checkargs(3,"frg","e4",4,2)


# In[54]:


def f(a,b,c):
    print("A is:",a)
    print("B is:",b)
    print("C is:",c)


# In[55]:


f(2,4,5)


# In[57]:


#f(2,5,"fg")
f(5,"fg", 2)


# In[58]:


f(a=2, b= 5, c="dh")


# In[59]:


f(b= 5, c="dh",a=2)


# In[64]:


def add(x,y):
    c=x+y
    print(c)
    


# In[65]:


add(5,6)


# # Function return 

# In[74]:


def myadd(a,b):
    sumvalue=a+b
    return sumvalue
    


# In[75]:


d=myadd(2,3)


# In[76]:


print(d)


# In[77]:


variableOutsideTheFunction=3


# In[78]:


def g():
    print(variableOutsideTheFunction)


# In[79]:


g


# In[80]:


g()


# In[87]:


def g():
    variableOutsideTheFunction=5
    #print(variableOutsideTheFunction)


# In[82]:


g()


# In[83]:


print(variableOutsideTheFunction)


# In[88]:


print(type(g()))


# In[93]:


def h():
    print("A")
    a=2
    b=5
    c=a+b
    print("Smoething")
    return
    print("B")
    print("C")


# In[94]:


h()


# In[95]:


def h():
    print("A")
    a=2
    b=5
    c=a+b
    print("Smoething")
    return c
    print("B")
    print("C")


# In[96]:


h()


# In[97]:


def h():
    print("A")
    a=2
    b=5
    c=a+b
    print("Smoething")
    #return
    print("B")
    print("C")


# In[98]:


h()


# In[99]:


def r():
    a=5
    b=7
    d="something"
    return a,b,d


# In[100]:


r()


# In[101]:


x,y,z=r()


# In[102]:


x


# In[103]:


y


# In[104]:


z


# In[105]:


print(x,y,z)


# #  Functions (variable number of input arguments)
# 

# In[ ]:


def add(*args):
    sum=0
    for i in range(len(args)):
        sum+=args[i]
    return sum


# In[ ]:


add(3,4,5,6,7)


# In[ ]:


sum=add(455,56)


# In[ ]:


print(sum)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'args')


# In[18]:


def printallvariablesnamesandvalues(**args):
    for x in args:
        print("Variable name is :" ,x, "and value is:", args[x])


# In[21]:


printallvariablesnamesandvalues(a=4,b=78,c="cccc", j="drfgf", er=56)


# In[1]:


$a=d+g-t


# # Functions( Default values)

# In[6]:


def gg(s=4):
    print(s)


# In[7]:


gg()


# In[8]:


gg(45)


# In[9]:


L=[1,2,3]
L2=L
L2[0]=-9
print(L)


# In[10]:


L=[1,2,3]


# In[11]:


L2=L


# In[12]:


L2


# In[13]:


L2[0]=-9


# In[14]:


L


# In[15]:


def ff(L=[1,2]):
    for i in L:
        print(i)


# In[16]:


ff()


# In[17]:


L2=[12,3,45]


# In[18]:


ff(L2)


# In[19]:


ff()


# In[37]:


def myAddUniversal(*args):
    s=0
    for i in range(len(args)):
        s+=args[i]
    return s


# In[38]:


myAddUniversal(4,5,6,7)


# In[29]:


sum


# In[30]:


def add(*args):
    sum=0
    for i in range(len(args)):
        sum+=args[i]
    return sum


# In[31]:


add(2,4,5,5,2)


# In[6]:


import sys
sys.path.append(r'C:/abc/')


# In[8]:


import My_module


# # Practice Functions
# 

# In[49]:


""" Given a list of numbers i.e. [1,2,4,-5,7,9,3,2], make another list that contains all the items in sorted order 
from min to max i.e your results will be another list like [-5,1,2,3,4,5,7,9]

"""

L=[1,2,4,-5,7,9,3,2]
for j in range(len(L)):
    m=L[j]
    idx=j
    c=j
    for i in range(j,len(L)):
        if L[i]<m:
            m=L[i]
            idx=c
        c+=1
    tmp=L[j]
    L[j]=m
    L[idx]=tmp
print(L)

        


# In[52]:


def findMin(L):
    m=L[0]
    idx=0
    i=0
    for x in L:
        if x<m:
            m=x
            idx=i
        else:
            pass
        i+=1
    return m, idx
        


# In[53]:


a,b=findMin([2,4,4,0,9])


# In[54]:


print(a,b)


# In[17]:



def swapValues(L,idx1,idx2):
    tmp=L[idx1]
    L[idx1]=L[idx2]
    L[idx2]=tmp

    return L


# In[18]:


L=[2,3,5,0,8]


# In[19]:


L2=swapValues(L,1,3)


# In[20]:


L2


# In[21]:


from My_module import checkIfNotNumeric
def sortList(L):
    if not(checkIfNotNumeric(L)):
        print("Error: List does not contain numeric values")
        return
    else:
        c=0
        for x in L:
            m,idx=findMin(L)
            L=swapValues(L,c,idx)
            c+=1
    return L


# In[22]:


L2=sortList([2,4,5,26,7,777])
print(L2)


# In[15]:


from My_module import checkIfNotNumeric


# In[1]:


L=[1,23,4,4,5,6,7,8,9,3,4]


# In[2]:


L


# In[3]:


type(L)


# In[4]:


pop(L)


# In[5]:


.pop(L)


# In[6]:


L.pop()


# In[7]:


L


# In[8]:


L.soda()


# In[9]:


L.cola()


# In[10]:


L.drink()


# In[11]:


L.fizzbuzz()


# In[12]:


L.pop()


# In[13]:


L.pop()


# In[15]:


L.pop()


# In[16]:


L.pop()


# In[17]:


L.pop()


# In[18]:


L.pop()


# In[19]:


L.pop()


# In[20]:


L.pop()


# In[21]:


L.pop()


# In[22]:


L.pop()


# In[23]:


L.pop()


# In[24]:


a = [‘mn’, ‘op’]
for i in a:
    i.upper()
    print(a)


# In[25]:


a=['mn','op']
for i in a:
    i.upper()
    print(a)


# In[31]:


a=['mn','op','rt']
for i in a:
    a.upper()
    print(a)


# In[32]:


i='hello'
print(i.upper())


# In[33]:


a=['mn','op','rt']
print(a.upper())


# In[1]:


from TVDI_IPython_Interface import TVDI_IPython_Interface # import the TVDI class object
setup=TVDI_IPython_Interface() # Create the setup instance from the PyTSEB class object
setup.TVDIWidget() # Load the TVDI configuration Widget


# In[1]:


get_ipython().run_line_magic('pinfo', 'urllib.parse')


# In[2]:


pip install pystac


# In[3]:


pip install pystac[validation]


# In[1]:


pip install urllib.parse


# In[ ]:




