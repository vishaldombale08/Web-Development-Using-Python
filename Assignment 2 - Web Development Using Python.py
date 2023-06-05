#!/usr/bin/env python
# coding: utf-8

# In[7]:


#1. Write a python script to add comments and print “Learning Python” on screen.

#"Learning Python"
print("above is lerning python comment which is not prinable")


# In[ ]:


Write a python script to add multi line comments and print values of four variables,
each in a new line. Variable contains any values.

"""
a = 10
b = 20
c = 30
d = 40
"""


# In[21]:


#3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)

a = 35
b = True
c = "MySirG"
d = 5.46
e = 3+4j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# In[23]:


#4. Write a python script to print the id of two variables containing the same integer values.

a =5
b =5

print(id(a))
print(id(b))


# In[8]:


#5. Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable

a = 3
b = "vishal"
c = True
d = 3+4j
e = 4.6

print(a, type(a), id(a))
print(b, type(b), id(b))
print(c, type(c), id(c))
print(d, type(d), id(d))
print(e, type(e), id(e))


# In[24]:


#6. Write a python script to print all the keywords
import keyword
print(keyword.kwlist)


# In[ ]:


#7. On Python shell use help() function and display the list of keywords

#i have used it in python shell 

help()
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

# i have get the output like all keywords


# In[10]:


"""10.Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py"""

#stored in A1 file

x=10
print(x)

#importe A1 file in A0 file get printed its output

import A1
print(A1.x)


# In[11]:


#9. Name the keywords, used as data in the Python script.

True
False
None


# In[12]:


"""10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)"""

from datetime import datetime
dt = datetime.today();

d1 = dt.strftime("%d-%m-%Y and %I:%M %p")
print(d1)


# In[ ]:




