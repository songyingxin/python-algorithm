# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)

        return left_depth+1 if left_depth > right_depth else right_depth+1


        