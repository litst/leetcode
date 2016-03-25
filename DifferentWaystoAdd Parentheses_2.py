# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 15:18:51 2016

@author: yzy
"""

def f(opers,nums):
    print opers,nums
    if(len(opers)>0):
        for i in xrange(len(opers)):
            if opers[i] == "+":
                f(opers[:i]+opers[i+1:],nums[:i]+[nums[i]+nums[i+1]]+nums[i+2:])
            elif opers[i] == "-":
                f(opers[:i]+opers[i+1:],nums[:i]+[nums[i]-nums[i+1]]+nums[i+2:])
            elif opers[i] == "*":
                f(opers[:i]+opers[i+1:],nums[:i]+[nums[i]*nums[i+1]]+nums[i+2:])
    else:                
        ans.append(nums[0])

input = "1+2+3"            
opers = []
opersLoc = []
nums = []
ans = []
for i in xrange(1,len(input)):
    if input[i] in ['+','-','*']:
        opersLoc.append(i)
        opers.append(input[i])
if len(opers) == 0:
    ans.append(int(input))
else:
    nums.append(int(input[:opersLoc[0]]))
    for i in xrange(len(opersLoc)-1):
        nums.append(int(input[opersLoc[i]+1:opersLoc[i+1]]))
    nums.append(int(input[opersLoc[-1]+1:]))
    f(opers,nums)
print ans