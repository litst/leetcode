# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 15:20:04 2016

@author: yzy
"""

def f(n):
    sum = 0
    if n > 0:
       
        mode = [0]*n
        for i in xrange(n):
            for k in xrange(1,n/(i+1)+1):
           
            
                mode[k*(i+1)-1] += 1
                k += 1
        for i in xrange(n):
            if mode[i]%2 == 1:
                sum += 1
    return sum          
print f(999999)