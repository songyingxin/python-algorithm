# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        
        if pRoot.left and not pRoot.right:
            return False
        
        if not pRoot.left and pRoot.right:
            return False
        
        return self.is_same(pRoot.left, pRoot.right)


    def is_same(self, p1, p2):
        """
        判断两棵树是否对称
        """
        if not p1 and not p2:
            return True
        
        if (p1 and p2) and p1.val == p2.val:
            return self.is_same(p1.left, p2.right) and self.is_same(p1.right, p2.left)
        