# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.is_same(pRoot, pRoot)


    def is_same(self, p1, p2):
        """
        判断两棵树是否对称
        """
        if not p1 and not p2:
            return True
        
        if not p1 or not p2:
            return False
        
        if p1.val != p2.val:
            return False
        
        return self.is_same(p1.left, p2.right) and self.is_same(p1.right, p2.left)