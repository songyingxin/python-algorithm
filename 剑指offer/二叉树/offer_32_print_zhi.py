# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        res = []

        is_zheng = True
        while queue:
            tmp_res = []
            tmp_queue = []

            for node in queue:
                tmp_res.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                
                if node.right:
                    tmp_queue.append(node.right)
            if is_zheng:
                res.append(tmp_res)
            else:
                res.append(tmp_res[::-1])
            is_zheng = not is_zheng
            queue = tmp_queue
        
        return res