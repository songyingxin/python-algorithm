# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_distance = 1

        def depth(node):
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            self.max_distance = max(self.max_distance, left_depth + right_depth + 1)
    
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.max_distance - 1
