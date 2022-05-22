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
        queue = [pRoot]
        left_to_right = True
        res = []
        
        while queue:
            tmp_queue = []
            tmp_res = []
            for node in queue:
                tmp_res.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            
            if left_to_right:
                res.append(tmp_res)
            else:
                res.append(tmp_res[::-1])
            left_to_right = not left_to_right
            queue = tmp_queue
        return res
