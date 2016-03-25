# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:07:13 2015

@author: yzy
"""
nums = [2,1,1]
ans = 0
for i in range(len(nums)):
    nums[(nums[i]-1) % len(nums)] += len(nums)
for i in range(len(nums)):
    if nums[i] > 2*len(nums):
        ans = i + 1
        nums[i] -= len(nums)
for i in range(len(nums)):
    while nums[i] > len(nums):
        nums[i] -= len(nums)
print ans