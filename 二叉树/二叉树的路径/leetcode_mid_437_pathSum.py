class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def dfs(node, target):
            if not node:
                return 0
            
            target -= node.val

            res = 1 if target == 0 else 0
            left_count = dfs(node.left, target)
            right_count = dfs(node.right, target)

            return res + left_count + right_count
        
        root_num = dfs(root, targetSum)
        left_num = self.pathSum(root.left, targetSum)
        right_num = self.pathSum(root.right, targetSum)
        return  root_num + left_num + right_num
