# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node):
            if not node:
                return 0
            
            return max(depth(node.left), depth(node.right)) + 1

            
        if not root:
            return True

        left_depth = depth(root.left)
        right_depth = depth(root.right)
        
        return abs(left_depth-right_depth) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right) 