# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 10:17:43 2016

@author: yzy
"""
def f(qn,al):
    if len(qn) == n:
        r = []
        for j in xrange(len(qn)):
            s = '.'*qn[j]+'Q'+'.'*(n-1-qn[j])
            r.append(s)
        res.append(r)
    else:
        for i in xrange(len(al)):
            
            iv = True
            for j in xrange(len(qn)):
                
                if abs(al[i]-qn[j]) == abs(len(qn)-j):
                    
                    iv = False
            if iv == True:   
                
                f(qn+[al[i]],al[:i]+al[i+1:])
        

res = []       
n = 8
al = range(n)
for i in xrange(n):
    f([al[i]],al[:i]+al[i+1:])

print res
        