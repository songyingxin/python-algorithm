# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.dfs(root, 0)
        
        return root

    def dfs(self, node, sum_val):

        if not node:
            return sum_val
        
        sum_val = self.dfs(node.right, sum_val)

        node.val += sum_val
        
        sum_val = self.dfs(node.left, node.val)

        return sum_val