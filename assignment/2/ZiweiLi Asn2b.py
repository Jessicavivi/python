#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ziwei Li Assignment2b
temp = 0
print('Welcome to the 2-currency calculator! ')
amount = float(input('Please enter the From amount: '))
currency = input('Please enter the From currency (USD or EUR):')
exchange_rate = 1.10
if currency == 'USD':
    temp = amount * (1/exchange_rate)
    print(f'{amount:.2f}USD equals{temp:.2f}EUR')
else :
    temp = amount * exchange_rate
    print(f'{amount:.2f} EUR equals {temp:.2f} USD ')

