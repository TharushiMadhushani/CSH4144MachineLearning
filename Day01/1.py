#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Hello world")


# x=5
# print(x)

# In[4]:


x=5
print(x)


# In[5]:


x="hello"
print(x)


# In[ ]:


x=int(5)
x=str("hello")


# In[6]:


x=5
print(type(x))


# In[7]:


x=5.5


# In[8]:


x=5.5
print(type(x))


# In[9]:


x=3.1111111111111111111111111111
print(type(x))


# In[10]:


x=3.11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
print(type(x))


# In[11]:


x='c'
print(type(x))


# In[12]:


x="c"
print(type(x))


# In[13]:


x='c'
print(type(x))


# In[14]:


x=4
y=2
add=x+y
sub=x-y
mul=x*y
div=x/y
print(add)
print(sub)
print(mul)
print(div)


# In[15]:


myclass=5
_myclass=5


# In[16]:


#commands


# In[18]:


age=6
Age=7
AGE=8
print(age,Age,AGE)
print(age+Age+AGE)


# In[20]:


x="Good"
def myfun():
    print(x)
myfun()


# In[23]:


a=2
b=12
if a>b:
    print("a is greater than b")
    
elif a==b:
    print("a and b are an equal")
    
else:
    print("b is greater than a")


# In[25]:


#while loop
i=1
while i<6:
    print(i)
    i+=1


# In[26]:


#for loop
letters=["A","B","C","D"]
for x in letters:
    print(x)


# In[28]:


#banana
for x in "banana":
    print(x)


# In[30]:


letters=["A","B","C","D"]
for x in letters:
    print(x)
    
    if x=="C":
        break


# In[32]:


letters=["A","B","C","D"]
for x in letters:
    
    if x=="C":
        continue
        
print(x)


# In[35]:


for x in range(1,6):
    print(x)


# In[37]:


letters=["A","B","C","D"]
numbers=[1,2,3,4,5]
for x in letters:
    for y in numbers:
        print(x,y)


# In[39]:



def myfun(fname):
    print("hi I am "+fname)
myfun("Anjalee")


# In[43]:


def myfun(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    rem=a%b
    print("addition is :",add)
    print("subtraction is :",sub)
    print("multiplication is :",mul)
    print("division is :",div)
    print("remainder is :",rem)
myfun(4,2)
    


# In[47]:


from statistics import median,mode,mean,stdev
data=[1,2,3,4,5,6,7,8,9]

result=median(data)
print("Median: ",result)

print("Mean: ",mean(data))
print("Mode: ",mode(data))
print("Stdev: ",stdev(data))


# In[49]:


from statistics import median,mode,mean,stdev
data=[90,67,78,23,56,86,96,56,45]

result=median(data)
print("Median: ",result)

print("Mean: ",mean(data))
print("Mode: ",mode(data))
print("Stdev: ",stdev(data))


# In[ ]:




