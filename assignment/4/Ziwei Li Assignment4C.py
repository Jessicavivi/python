#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Ziwei Li Assignment4C

def leap_year(year):
   if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               return False  
           else:
               return True
       else:
           return False      
   else:
       return True 
def trans():
   month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
   index = int(date[0])-1
   print(month[index],'/',day,'/',year)
   
date = input('Please enter a date of form mm/dd/yyyy:')
date = date.split('/')



day = int(date[1])
m = int(date[0])
year = int(date[2])
if len(date) != 3:
   print('Invalid date format ')
   quit()
elif m == 2  and leap_year(year) and day >= 29:
   print(f'Invalid day:{day}')
   quit()

elif m in [1,3,5,7,8,10,12] and day >= 31:
   print(f'Invalid day:{day}')
   quit()
   
elif m in [4,6,9,11] and day >= 30:
   print(f'Invalid day:{day}')
   quit()
elif m > 12:
   print(f'Invalid day for given month:{m}')
   quit()
else:trans()

