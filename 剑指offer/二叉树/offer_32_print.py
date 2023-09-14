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

        res = []
        queue = [root]

        while queue:
            tmp = []
            queue_tmp = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    queue_tmp.append(node.left)
                
                if node.right:
                    queue_tmp.append(node.right)
            
            res.append(tmp)
            queue = queue_tmp
        
        return res

