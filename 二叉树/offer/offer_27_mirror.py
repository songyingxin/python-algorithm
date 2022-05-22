# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # write code here
        if not pRoot:
            return 
        
        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
        
        return pRoot




