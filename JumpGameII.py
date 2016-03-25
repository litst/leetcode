# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 14:13:32 2015

@author: yzy
"""

def subJump(nums,step,ans):
   
    maxStep = nums[0]
    
    for i in range(1,maxStep+1):
        
        if len(nums[i:]) == 1:
            ans.append(step+1)
        else:
            if i < len(nums) and nums[i] != 0 :
                subJump(nums[i:],step+1,ans)
       
   
       
                        
nums = [6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]
ans = []           
subJump(nums,0,ans)
print min(ans)
