

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        def dfs(node, sum_val):
            if not node:
                return 0
            
            res = 1
            sum_val += node.val

            res = 1 if sum_val == sum else 0
            res += dfs(node.left, sum_val) + dfs(node.right, sum_val)
            return res
            
        return dfs(root, 0) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)










