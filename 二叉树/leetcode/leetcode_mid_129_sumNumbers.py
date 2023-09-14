
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        res = []
        def dfs(root, root_val):
            if not root:
                return
            
            if not root.left and not root.right:
                root_val = root_val * 10 + root.val
                res.append(root_val)
                return 
            
            root_val = root_val * 10 + root.val
            
            dfs(root.left, root_val)
            dfs(root.right, root_val)
        
        dfs(root, 0)
        return sum(res)
