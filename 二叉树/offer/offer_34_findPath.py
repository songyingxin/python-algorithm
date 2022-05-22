# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def FindPath(self , root: TreeNode, target: int) -> List[List[int]]:
        # write code here
        res = []
        def find_path(root, target, path):
            if not root:
                return None
            if not root.left and not root.right:
                if target == root.val:
                    res.append(path)
            path.append(root.val)
            find_path(root.left, target-root.val, path[:])
            find_path(root.right, target-root.val, path[:])
        find_path(root, target, [])
        
        return res