#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ziwei Li Asn5a
def NetPresentValue(cashflow,rate):
    t = 1
    sum = 0
    for c in cashflow:
        p = c/(1 + rate)**t
        sum += p
        t += 1
    return sum

print("%.2f" % NetPresentValue([0, 100], .05))        
print("%.2f" % NetPresentValue([4, 4, 4, 104], .05))         
print("%.2f" % NetPresentValue([], .05))  

