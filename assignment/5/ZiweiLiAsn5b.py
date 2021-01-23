#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ziwei Li Assignment5b 
def CalcMode(list1):
    if len(list1) == 0:
        return []
    dictNum = {}
    for i in list1:
        if i in dictNum.keys():
            dictNum[i] = dictNum[i] + 1
        else:
            dictNum[i] = 1
    maxValue = max(dictNum.values())
    list2=[]
    for j in dictNum.keys():
        if dictNum[j] == maxValue:
            list2.append(j)
    return list2
print(CalcMode([1, 2, 3, 2]))
print(CalcMode([1, 2, 1, 2]))
print(CalcMode([]))

