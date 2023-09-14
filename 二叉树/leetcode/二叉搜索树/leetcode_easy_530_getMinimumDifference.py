

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.min_abs = float('inf')
        self.pre_val = -100000

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            now_abs = node.val - self.pre_val
            self.min_abs = min(now_abs, self.min_abs)
            self.pre_val = node.val
            dfs(node.right)
        
        dfs(root)
        return self.min_abs