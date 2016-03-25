# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:37:44 2015

@author: yzy
"""
n = 150000
count = 0
for i in range(2,n):
    isPrime = True
    for j in range(2,int(round(i**0.5))+1):
        if i % j == 0:
            #print i ,j
            isPrime = False
    if isPrime == True:
        count += 1

print count    