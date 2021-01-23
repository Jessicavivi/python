#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ziwei Li Assignment2c
temp = 0
print('Welcome to the 3-currency calculator! ')
amount = float(input('Please enter the From amount: '))
currency1 = input('Please enter the From currency ((USD, EUR, or RMB):')
currency2 = input('Please enter the To currency (USD, EUR, or RMB): ')
EU_rate = 1.10
RU_rate = 0.14
RE_rate = 0.13
if currency1 == 'USD' and currency2 == 'EUR':
    temp = amount * (1/EU_rate)
    print(f'{amount:.2f} {currency1} equals {temp:.2f} {currency2}')
elif currency1 == 'EUR' and currency2 == 'USD':
    temp = amount * EU_rate
    print(f'{amount:.2f} {currency1} equals {temp:.2f} {currency2}')
elif currency1 == 'RMB' and currency2 == 'EUR':
    temp = amount * RE_rate
    print(f'{amount:.2f} {currency1} equals {temp:.2f} {currency2}')
elif currency1 == 'EUR' and currency2 == 'RMB':
    temp = amount * (1/RE_rate)
    print(f'{amount:.2f} {currency1} equals {temp:.2f} {currency2}')
elif currency1 == 'RMB' and currency2 == 'USD':
    temp = amount * RU_rate
    print(f'{amount:.2f} {currency1} equals {temp:.2f} {currency2}')
else:
    temp = amount * (1/RU_rate)
    print(f'{amount:.2f} {currency1} equals {temp:.2f} {currency2}')


# In[ ]:




