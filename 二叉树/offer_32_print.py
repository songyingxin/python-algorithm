# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        res = []
        queue = [pRoot]

        while queue:
            current_size = len(queue)

            current_vals = []
            for i in queue:
                current_vals.append(i.val)
            
            res.append(current_vals)
            for i in range(current_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
            
