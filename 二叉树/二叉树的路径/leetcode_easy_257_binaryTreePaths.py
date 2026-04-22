class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        self.res = []

        def dfs(node,item):
            if not node:
                return 
            
            item.append(str(node.val))
            if not node.left and not node.right:
                self.res.append('->'.join(item))
                return 
            
            dfs(node.left, item[:])
            dfs(node.right,item[:])
        
        dfs(root, [])
        return self.res