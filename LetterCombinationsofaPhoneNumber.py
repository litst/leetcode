# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 20:29:13 2016

@author: yzy
"""

d = {'2':['a','b','c'],
     '3':['d','e','f'],
     '4':['g','h','i'],
     '5':['j','k','l'],
     '6':['m','n','o'],
     '7':['p','q','r','s'],
     '8':['t','u','v'],
     '9':['w','x','y','z']
}
def f(digits,a):
    for i in digits:
        dd = []
        for k in a:
            for j in d[i]:
                dd.append(k+j)
        a = dd
    return dd

digits = '222'   
a = []            
if len(digits) == 0:
    print a
else:
    for i in d[digits[0]]:
        a.append(i)
    if len(digits) == 1:
        print a
    else:
        a = f(digits[1:],a)
        print a