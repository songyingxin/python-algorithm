# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def helper(node):
            if not node:
                return 0, 0
            
            left_distance, left_depth = helper(node.left)
            right_distance, right_depth = helper(node.right)

            distance = max(left_distance, right_distance, left_depth + right_depth + 1)
            depth = max(left_depth, right_depth) + 1

            return distance, depth
        
        distancce, _ = helper(root)

        return distancce
