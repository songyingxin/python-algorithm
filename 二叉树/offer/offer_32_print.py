# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        # write code here
        if not pRoot:
            return []
        
        res = []
        queue = [pRoot]
        while queue:
            tmp_queue = []
            tmp_res = []
            for node in queue:
                tmp_res.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            res.append(tmp_res)
            queue = tmp_queue
        return res
