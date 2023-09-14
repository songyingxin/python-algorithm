# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
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

            queue = tmp_queue
            res.append(tmp_res)
        
        return res


