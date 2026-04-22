class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.p = p
        self.q = q

        def dfs(node):
            if not node:
                return 
            
            if node == self.p or node == self.q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            
            return left if left else right
        return dfs(root)
