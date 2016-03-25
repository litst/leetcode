# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:55:22 2016

@author: yzy
"""

n = 1
d = 90
ys = []
r = ''
l = 0
while n < d:
    n *= 10
    l += 1
a = n/d
n -= a*d

while n not in ys and n > 0:
    ys.append(n)
    if l == 0:
        r += str(a)
    else:
        if '.' in r:
            r += '0'*(l-1)+str(a)
        else:
            r +='.'+'0'*(l-1)+str(a)
    l = 0
    while n < d:
        n *= 10
        l += 1
    a = n/d
    n -= a*d
   
    
if r[0] == '.':
    r = '0' + r
print r
if n > 0:
    j = -1
    for k in xrange(len(r)):
        if r[k] == '0' or r[k] == '.':
            j += 1
        else:
            break
    
    i = ys.index(n)
    
    if r[0] == 0:
        r = r[:1+i] + '(' + r[1+i:] + ')'
    else:
        r = r[:2+i] + '(' + r[2+i:] + ')'
print r
