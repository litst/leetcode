# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 20:12:38 2016

@author: yzy
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


ans = []
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    
    if root != None:
        inorderTraversal(root.left)
        ans.append(root.val)
        inorderTraversal(root.right)
    return ans

a = TreeNode(1)
a.left = TreeNode(2)
a.left.right = TreeNode(3)
print inorderTraversal(a)