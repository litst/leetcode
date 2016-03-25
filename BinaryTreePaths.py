# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:11:37 2015

@author: yzy
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def dfs(root):
    ans = []
    if root.left != None:
        for subStr in dfs(root.left):
            ans.append(str(root.val)+'->'+subStr)
    if root.left == None:
        ans.append(str(root.val))
    if root.right != None:
        for subStr in dfs(root.right):
            ans.append(str(root.val)+'->'+subStr)
    return ans
    
root = TreeNode(1)

l1 = None
r2 = TreeNode(3)
root.left = l1
root.right = r2
if str(root.val) in dfs(root):
    dfs(root).remove(str(root.val))
ans = dfs(root)