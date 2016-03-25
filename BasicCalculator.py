# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:48:35 2016

@author: yzy
"""
def cal(s):
    if ('+' not in s and '-' not in s) or (s[0] == '-' and '+' not in s[1:] and '-' not in s[1:]):
        return int(s)
    else:
        for i in xrange(1,len(s)):
            if s[i] == '+':
                if s[i+1] == '-':
                    return int(s[:i])-cal(s[i+2:])
                return int(s[:i])+cal(s[i+1:])
                
            if s[i] == '-':
                if s[i+1] == '-':
                    return int(s[:i])+cal(s[i+2:])
                return int(s[:i])-cal(s[i+1:])
                
i = 0
a = []
s = "1-2+3"
while i < len(s):
    if s[i] == '(':
        a.append(i)
        i += 1
    if s[i] == ')':
        j = a[-1]
        a.remove(j)

        s = s[:j]+str(cal(s[j+1:i]))+s[i+1:]
        i = j
       
    else:
        i += 1
print cal(s)
        
