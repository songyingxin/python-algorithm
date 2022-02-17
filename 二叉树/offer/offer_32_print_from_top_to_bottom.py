# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        if not root:
            return res

        queue = [root]

        while queue:
            now_node = queue.pop(0)
            res.append(now_node.val)

            if now_node.left:
                queue.append(now_node.left)
            
            if now_node.right:
                queue.append(now_node.right)
            
        return res
        


        
