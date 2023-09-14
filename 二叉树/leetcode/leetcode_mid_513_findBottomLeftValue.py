# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 

        res = None
        queue = [root]

        while queue:
            res = queue[0].val
            tmp_queue = []
            for node in queue:
                if node.left:
                    tmp_queue.append(node.left)
                
                if node.right:
                    tmp_queue.append(node.right)
            
            queue = tmp_queue
        
        return res