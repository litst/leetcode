# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:53:08 2015

@author: yzy
"""

from numpy import *

data = [0,1,0,2,1,0,1,3,2,1,2,1]

maxHeight = max(data)
minHeight = min(data)

def findBounds(index,curHeight,data):
    left = -1
    right = -1
    for i in range(index):
        if data[index-i-1] > curHeight:
            left = index-i-1
            break
    
    for i in range(index+1,len(data)):
        if data[i] > curHeight:
            right = i
            break
    
    return left,right
           
sum = 0
    
for i in range(minHeight,maxHeight+1):
    for j in range(1,len(data)):
        if data[j] == i:
            l,r = findBounds(j,i,data)
            if l!=-1 and r!=-1:
                for k in range(l,r+1):
                    if data[k] == i:
                        data[k] += 1
                        sum += 1
                        print j,l,r,sum
            
print sum
        
    