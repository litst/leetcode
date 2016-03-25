# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:49:18 2015

@author: yzy
"""
nums = [1,2]
for i in range(len(nums)-1,-1,-1):
    if i == 0:
        nums.sort()
    elif nums[i]>nums[i-1]:
        subNums = nums[i:]
        subNums.sort()
        nums[i:] = subNums
        print nums[i:]
        nums[i],nums[i-1] = nums[i-1],nums[i]
        print nums
print nums
        