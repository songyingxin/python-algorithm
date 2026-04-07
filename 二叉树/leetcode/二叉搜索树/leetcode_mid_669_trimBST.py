class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return
            
            if node.val < low:
                return dfs(node.right)
            
            if node.val > high:
                return dfs(node.left)
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            return node
        
        root = dfs(root)
        return root