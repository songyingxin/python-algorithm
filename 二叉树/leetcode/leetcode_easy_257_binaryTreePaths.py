class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        res = []
        def dfs(node, path):
            if not node:
                return 

            path.append(str(node.val))
            if not node.left and not node.right:
                path = '->'.join(path)
                res.append(path)
                return
            
            dfs(node.left, path[:])
            dfs(node.right, path[:])
        
        dfs(root, [])
        return res