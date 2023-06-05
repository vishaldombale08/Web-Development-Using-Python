#!/usr/bin/env python
# coding: utf-8

# In[9]:


#1. Write a python script to convert a number into str type.

x = 10
print(type(str(x)))


# In[13]:


#2. Write a python script to print Unicode of the character ‘m’
print(ord("m"))


# In[14]:


#3. Write a python script to print character representation of a given unicode 100.
print(chr(100))


# In[ ]:


#4. Write a python script to print any number and its binary equivalent

a =int(input())
print(bin(a))


# In[2]:


#5. Write a python script to print any number and its octal equivalent.

a =int(input())
print(oct(a))


# In[3]:


#6. Write a python script to print any number and its hexadecimal equivalent.
a =int(input())
print(hex(a))


# In[6]:


#7. Write a python script to store binary number 1100101 in a variable and print it in decimal format.
a = 0b1100101
print (a)


# In[7]:


#8. Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
a = 0x2F
print(a)


# In[8]:


#9. Write a python script to store an octal number 125 in a variable and print it in binary format.
a = 0o125
print(a)


# In[23]:


#10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format.

a = 0o25
b = 0x39

r = bin(a)+bin(b)
print(r)


# In[ ]:




