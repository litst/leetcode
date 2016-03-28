# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
       
        def f(il,ir,pl,pr):
            root  = None
            if il != ir:
                rootVal = postorder[pr-1]
                rlocation = inorder.index(rootVal)
                '''
                lio = inorder[il:rlocation]
                rio = inorder[rlocation+1:ir]
                lpo = postorder[pl:pl+rlocation-il]
                rpo = postorder[pl+rlocation-il:pr-1]
                '''
                root = TreeNode(rootVal)
                root.left = f(il,rlocation,pl,pl+rlocation-il)
                root.right = f(rlocation+1,ir,pl+rlocation-il,pr-1)
            return root
        return f(0,len(inorder),0,len(inorder))
            