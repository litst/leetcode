# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 18:38:24 2015

@author: yzy
"""
from numpy import *

matrix = [[1,0,1,0,0],
          [1,0,1,1,1],
          [1,1,1,1,0],
          [1,0,0,0,1]]


n = len(matrix)
m = len(matrix[0])
widths = [0] * n
k = 0
for j in xrange(0, m):
    max_continous_k = 0
    continous_k = 0
    for i in xrange(0, n):
        if matrix[i][j] == 1:
            widths[i] += 1
        else:
            widths[i] = 0
        if widths[i] > k:
            continous_k += 1
            max_continous_k = max(continous_k, max_continous_k)
        else:
            continous_k = 0
    if max_continous_k > k:
        k += 1
print k * k