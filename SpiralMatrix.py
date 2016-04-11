# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:12:45 2016

@author: yzy
"""
matrix = [[7],[9],[6]]
ans = []
        
def xprint(index,length,high):
    for i in range(length):
        ans.append(matrix[index][index+i])
    if high > 1:
        for i in range(1,high):
            ans.append(matrix[index+i][index+length-1])
        if length > 1:
            for i in range(1,length):
                ans.append(matrix[index+high-1][index+length-1-i])
            for i in range(1,high-1):
                ans.append(matrix[index+high-1-i][index])
high = len(matrix)
if high == 0:
    print []
length = len(matrix[0]) 
i = 0
while(min(high,length)>0):
    xprint(i,length,high)
    length -= 2
    high -= 2
    i += 1
print ans