# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here

        is_banlance, tree_depth = self.tree_depth(pRoot)

        return is_banlance

    def tree_depth(self, pRoot):

        if not pRoot:
            return True, 0

        left_banlance, left_depth, = self.tree_depth(pRoot.left)
        right_banlance, right_depth = self.tree_depth(pRoot.right)

        if abs(left_depth - right_depth) <= 1 and left_banlance and right_banlance:
            is_banlance = True
        else:
            is_banlance = False

        tree_depth = max(left_depth, right_depth) + 1
        return is_banlance, tree_depth
