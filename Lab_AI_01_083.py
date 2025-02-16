#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# print:
print("HELLLLOOO WORLLDDDD")

#VARIABLE DECLARATION
x = 5

#if-else:
if x > 2:
    print(x ,"is greater")
else:
    print("Five is smaller")


# In[20]:


# type-casting:
var_str = "333"
var_str_into_int = int(var_str)
print(type(var_str))
print(type(var_str_into_int))


# In[25]:


# multi-line comments:
'''hi this is multi line comment'''
i = 10
# WHILE LOOP:
while i > 0:
    print(i)
    i = i - 1


# In[26]:


# FOR-LOOP
for i in range(0,100):
    print("100 DAFA FOR BOLO")


# In[23]:


string = "hi i am here"
for i in string.split(" "):
    print(i)


# In[ ]:


# list
arr = [1,2,3,4]
for i in  arr:
    print(i)


# In[37]:


# set
sett = {1,2,3,7,5,3}
for i in  sett:
    print(i)


# In[38]:


#tuple
tpl = (1,44,22,55,33,4,232)
for i in  tpl:
    print(i)


# In[63]:


# dict
dct = {
    "a" : 500,
    "b" : False,
    "c" : "70"
}
for i,j in  dct.items():
    print("value for key {} is {} and its type is {}".format(i,j,type(j)))

# print keys
for i in dct:
    print(dct.get(i))


# In[58]:


l = [1,2,3]
l = tuple(l)
print(type(l))

fruits = ["apple","guava","mango"]
fruits = tuple(fruits)
print(type(fruits))


# In[71]:


class Stack:
    
    def __init__(self):
        self.stack = []
        
    def push(self,val):
        self.stack.append(val)
        
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.stack[len(self.stack)-1]
    

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.pop())
print(s.peek())

        

