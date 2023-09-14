# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        def is_sub(root_1, root_2):
            if not root_2:
                return True
            
            if not root_1 or root_1.val != root_2.val:
                return False
            
            return is_sub(root_1.left, root_2.left) and is_sub(root_1.right, root_2.right)
        
        if not A or not B:
            return False
        
        return is_sub(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)




