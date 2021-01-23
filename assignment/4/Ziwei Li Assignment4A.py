#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Ziwei Li Assignment4A
def transpose(matrix):
   transpose = [[[matrix[j][i] for j in range(len(matrix))] 
               for i in range(len(matrix[0]))]]
   for row in transpose:
       return row

print('matrix','[[1, 2, 3], [4, 5, 6]]')
print('transpose',transpose([[1,2,3], [4,5,6]]))

