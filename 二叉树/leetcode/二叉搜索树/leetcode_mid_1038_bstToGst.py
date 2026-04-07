# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.res = 0
        def dfs(node):
            if not node:
                return 
            dfs(node.right)
            node.val += self.res
            self.res = node.val
            dfs(node.left)
            
        
        dfs(root)
        return root
