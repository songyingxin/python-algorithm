class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def dfs(node, sum_val):
            if not node:
                return 0
            
            sum_val += node.val

            res = 1 if sum_val == targetSum else 0
            left_count = dfs(node.left, sum_val)
            right_count = dfs(node.right, sum_val)

            return res + left_count + right_count
        
        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
