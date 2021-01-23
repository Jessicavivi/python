#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Ziwei Li Assignment4B
import string

def main():
   l = s.lower() 
   for i in l:
       if i in string.punctuation:  
           l = l.replace(i,"")
   l = l.replace(' ','')
   if isPalindrome(l):
       print("That's a palindrome ")
   else:
       print("That's not a palindrome")
   
def isPalindrome(S):
   rev = ''.join(reversed(S)) 
   if (S == rev): 
       return True
   else:
       return False

while(1):
   s = input('Please enter a word or phrase, or to quit:')
   if len(s) != 0:
       main()
   else:
       break

