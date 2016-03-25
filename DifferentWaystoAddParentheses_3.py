# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 16:16:06 2016

@author: yzy
"""

def f(input):
    ans = []
    opLoc = []
    for i in xrange(len(input)):
        if input[i] in ["+","-","*"]:
            opLoc.append(i)
    if len(opLoc) == 0:
       
       ans.append(int(input))
    elif len(opLoc) == 1:
        i = opLoc[0]
        if input[i] == "+":
           
           ans.append(int(input[:i])+int(input[i+1:]))
        elif input[i] == "-":
           
           ans.append(int(input[:i])-int(input[i+1:]))
        elif input[i] == "*":
          
          ans.append(int(input[:i])*int(input[i+1:]))
    else:
        s = 0
        for i in xrange(len(opLoc)):
            for t in f(input[:opLoc[i]]):
                for k in f(input[opLoc[i]+1:]):
                    if input[opLoc[i]] == "+":
                       
                        s=t+k
                    elif input[opLoc[i]] == "-":
                        s=t-k
                    elif input[opLoc[i]] == "*":
                        s=t*k
            
                    ans.append(s)
    return ans
print f("2*3-4*5")
