# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def is_same(root_1, root_2):
            if not root_1 and not root_2:
                return True
            
            if not root_1 or not root_2:
                return False
            
            if root_1.val != root_2.val:
                return False
            
            return is_same(root_1.left, root_2.right) and is_same(root_1.right, root_2.left)
        
        return is_same(root, root)
