# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:26:42 2015

@author: yzy
"""
coins = [1,2,5]
amount = 100
d = {}
d[1] = coins
for i in xrange(2,amount/min(coins)+2):
    d[i] = []
    for k in d[i-1]:
        for t in coins:
                d[i].append(k+t)
    print d[i]
    if amount in d[i]:
        print i
        break
    if i == amount/min(coins)+1:
        print -1
