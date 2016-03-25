# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:13:50 2016

@author: yzy
"""

def f(s):
           
    op1 = ["+","-"]
    op2 = ["*","/"]
    i = 0
    while(i<len(s)):
        if s[i] in op2:
            if s[i] == "*":
                s = s[:i-1]+[s[i-1]*s[i+1]]+s[i+2:]
            else:
                s = s[:i-1]+[s[i-1]/s[i+1]]+s[i+2:]
        i += 1
    i = 0
    while(i<len(s)):
        if s[i] in op1:
            if s[i] == "+":
                s = s[:i-1]+[s[i-1]+s[i+1]]+s[i+2:]
            else:
                s = s[:i-1]+[s[i-1]-s[i+1]]+s[i+2:]
        i += 1
    return s[0]

s ="3+2*2"       
ans = []
ops = ["+","-","*","/"]
beg = 0
hasOps = False
for i in xrange(1,len(s)):
    if s[i] in ops:
        hasOps = True
        ans.append(int(s[beg:i]))
        ans.append(s[i])
        beg = i + 1
ans.append(int(s[beg:]))
print ans
if hasOps:
    print f(ans)
else:
    ans.append(int(s))
    print ans[0]