#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Ziwei Li Assignment 3c
password = input('Please enter the password: ')
count=0
while password !=  'pass1' and count < 2:
        password = input('This is incorrect,Please try again: ')
        count += 1
if password == 'pass1':
    print('Access granted.')
else:
    print('Access denied.')
    

