# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 21:00:58 2015

@author: yzy
"""

primes = [2,5]
n = 40
mode = {}
for i in xrange(len(primes)):
    mode[primes[i]] = primes[i:]
    
while(len(primes) < n-1):
    index = 0
    minValue = primes[0]*mode[primes[0]][0]
    for i in xrange(len(primes)):
        if minValue > primes[i]*mode[primes[i]][0]:
            minVale = primes[i]*mode[primes[i]][0]
            index = i
 
    del mode[primes[index]][0]
    
    if minValue not in primes:
        for i in xrange(len(primes)):
            #print minValue,mode[primes[i]],primes[i]
            if minValue not in mode[primes[i]] and minValue > primes[i]:
                mode[primes[i]].append(minValue)
                mode[primes[i]].sort()
        primes.append(minValue)
        primes.sort()
        mode[minValue] = primes[primes.index(minValue):]
        
    
