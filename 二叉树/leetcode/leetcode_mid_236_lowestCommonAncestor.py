# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return 

            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            
            if not left and right:
                return right
            
            if not right and left:
                return left
            
        return dfs(root)
