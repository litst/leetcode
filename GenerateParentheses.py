# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 20:58:15 2015

@author: yzy
"""

def geteSub(subStr,m,k,number):
    '''
    m:当前要插入“）”的位置
    number:剩余插入次数
    k:m之前的“（”个数与“（”个数之差
    '''
    if number == 0:
        ans.append(subStr)
    elif m == len(subStr)-1:
        geteSub(subStr+")"*number,m,k,0)
    elif k >0:
        geteSub(subStr[:m+1]+")"+subStr[m+1:],m+1,k-1,number-1)
        geteSub(subStr,m+1,k+1,number)
    elif k == 0:
        geteSub(subStr,m+1,1,number)
n = 3        
if n == 0:
    print []
ans = []    
geteSub("("*n,0,1,n)
print ans

