#!/usr/bin/env python
# coding: utf-8

# In[4]:


size = int(input('Enter size:'))
for i in range(1,size + 1):
    star_list = ['*'] * (size + 1 - i)
    for j in star_list:
        print('*',end = '')
    print()


# In[ ]:




