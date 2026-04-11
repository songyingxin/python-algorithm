class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            left = dfs(p.left,q.right)
            right = dfs(p.right,q.left)
            return left and right
        
        return dfs(root.left, root.right)