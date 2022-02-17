# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here

        if not root:
            return 
        root.left, root.right = root.right, root.left

        self.Mirror(root.left)
        self.Mirror(root.right)




