# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:04:09 2016

@author: yzy
"""


def help(i,ss,nums):
    if i<len(nums):
        if nums[i] != nums[i-1]:
            
            ans.append(ss+[nums[i]])
            
        help(i+1,ss,nums)
        help(i+1,ss+[nums[i]],nums)


snums = [4,1,0]
snums.sort()
ans = []
d = {}
for i in xrange(len(snums)-1):
    if snums[i] == snums[i+1]:
        d[snums[i]] = d.get(snums[i],1) + 1

for n in d:
    for i in xrange(d[n]):
        snums.remove(n)
if len(snums) == 1:
    ans = [[snums[0]]]
elif len(snums) > 1:
    help(0,[],snums)

ans.append([])
for term in d:
    cur = []
    for i in xrange(d[term]):
        cur.append([term]*(i+1))
        
    for i in xrange(len(ans)):
        for j in cur:
            if ans[i] != None:
                ans.append(sorted(ans[i]+j))
print ans