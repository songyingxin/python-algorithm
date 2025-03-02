# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1

        return max(left_depth, right_depth)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        max_depth = 0
        while stack:
            tmp_stack = []
            for val in stack:
                if val.left:
                    tmp_stack.append(val.left)
                if val.right:
                    tmp_stack.append(val.right)
            stack = tmp_stack
            max_depth += 1

        return max_depth