#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ziwei Li Assignment 3b
amount = float(input('Amount of starting investment ($):'))
term = int(input('Term of investment (# of years): '))
rate = float(input('Interest rate (%):'))
frequency = float(input('Compounding frequency (times/year): '))
year = input('Enter y if early termination:')
if year == 'n':
    for i in range(term):
        E = amount*(1 + 0.01*rate/frequency)**frequency
        interest = E - amount
        print('year\tstart balance\tinterest\tend balance')
        print(f'{i+1:.0f}\t{amount:.2f}\t\t{interest:.2f}\t\t{E:.2f}')
        amount = E
else :
    termination = int(input('Enter early termination year #: '))
    for i in range(termination):
        E = amount*(1 + 0.01*rate/frequency)**frequency
        interest = E - amount
        print('termination\tstart balance\tinterest\tend balance')
        print(f'{i+1:.0f}\t\t{amount:.2f}\t\t{interest:.2f}\t\t{E:.2f}')
        amount = E
    withdrawal = E*0.05
    final = E - withdrawal
    print(f'Early termination penalty ={withdrawal:.2f}')
    print(f'Adjusted final balance (after early withdrawal penalty) ={final:.2f}')


# In[ ]:




