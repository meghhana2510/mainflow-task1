#!/usr/bin/env python
# coding: utf-8

# variables and data types

# In[6]:


age = 25
height = 5.9
complex_number = 3 + 4j
print(f"Age: {age},Height: {height},Complex Number: {complex_number}, Type: {type(complex_number)}\n Type: {type(age)}\nType: {type(height)}\n")


# In[8]:


#stings
z="hello"
print(z)print(type(z))


# In[30]:


#list
x=[1,2,3,4,5]
print(x)
print(type(x))


# In[31]:


#list operations
# Append an element to the list
x.append(6)
print(x)  
# Access an element in the list 
element = x[2]
print(element) 
print(x) 
# Index val retreival
x = x[2]
print(x)  


# In[11]:


#tuple
y=(1,2,3,4,5)
print(y)
print(type(y))


# In[12]:


#dictionary
student = {
    "name": "Alice",
    "age": 22,
    "courses": ["Math", "Science"]
}
print(f"Student: {student}, Type: {type(student)}")


# In[13]:


#boolean

is_student = True
print(f"Is Student: {is_student}, Type: {type(is_student)}")


# In[ ]:




