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

        queue = [pRoot]
        while queue:
            vals = []
            for i in queue:
                vals.append(i.val)
            res.append(vals)
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            queue = tmp

        return res
