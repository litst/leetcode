# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 14:33:43 2016

@author: yzy
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def s(node):
    if node == None:
        return 0
    else:
        return node.val+max(max(0,s(node.left)),max(0,s(node.right)))
def sunSum(node):
    if node == None:
        return 0
    else:
        return node.val+max(0,s(node.left))+max(0,s(node.right))

def f(node):
    global m
    n = sunSum(node)
    if n > m:
        m = n
    if node.left != None:
        f(node.left)
    if node.right != None:
        f(node.right)
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)  
a.right.left = TreeNode(10)
a.right.right = TreeNode(20)      
m = 0
f(a)
print m