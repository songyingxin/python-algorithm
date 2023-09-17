class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.pre_val = 0
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            
            node.val = self.pre_val + node.val
            self.pre_val = node.val
            dfs(node.left)
            
        
        dfs(root)
        return root