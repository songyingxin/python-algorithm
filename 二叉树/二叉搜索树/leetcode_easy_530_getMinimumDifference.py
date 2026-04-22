

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.min_diff = float('inf')
        self.pre_val = None

        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if self.pre_val != None:
                self.min_diff = min(self.min_diff, node.val-self.pre_val)

            self.pre_val = node.val
            dfs(node.right)
        
        dfs(root)
        return self.min_diff