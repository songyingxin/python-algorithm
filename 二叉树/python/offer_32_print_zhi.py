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
        res = []
        if not pRoot:
            return res
        left_to_right = True
        queue = [pRoot]
        while queue:
            vals = []
            for i in queue:
                vals.append(i.val)
            if not left_to_right:
                vals = vals[::-1]
            res.append(vals)
            left_to_right = not left_to_right
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            queue = tmp

        return res
