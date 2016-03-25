# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:28:43 2015

@author: yzy
"""

nums = [1,2]
def findPeak(start,end):
    med = (start+end)/2
    if med == 0 and nums[med] > nums[med+1]:
        return med
    if med == len(nums)-1 and nums[med] > nums[med-1]:
        return med
    else:
        if nums[med-1] < nums[med] > nums[med+1]:
            return med
        elif nums[med+1] > nums[med]:
            return findPeak(med+1,end)
        else:
            return findPeak(start,med-1)
print findPeak(0,len(nums)-1)