# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)

        return root




