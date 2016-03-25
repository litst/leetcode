# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:56:28 2015

@author: yzy
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def dfs(start,end):
    ans = []
    if start == end:
        return None
    for i in range(start,end):
        for l in dfs(start,i) or [None]:
            for r in dfs(i+1,end) or [None]:
                node = TreeNode(i)
                node.left = l
                node.right = r
                ans.append(node)
    return ans

n = 3            
ans = dfs(1,n+1)
