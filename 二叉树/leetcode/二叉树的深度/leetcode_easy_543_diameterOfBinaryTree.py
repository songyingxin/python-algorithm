class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            self.res = max(self.res, left_depth + right_depth + 1)

            return max(left_depth, right_depth) + 1
        
        dfs(root)
        return self.res - 1
