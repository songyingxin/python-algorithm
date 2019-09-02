# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here

        if not root:
            return []
        
        res = []
        self.dfs(root, expectNumber, res, [])
        return res

    def dfs(self, root, expectNumber, res, path):
        path.append(root.val)

        if root.val == expectNumber and not root.left and not root.right:
            res.append(path)
        
        if root.left:
            self.dfs(root.left, expectNumber - root.val, res, path[:] )
        
        if root.right:
            self.dfs(root.right, expectNumber - root.val, res, path[:])
