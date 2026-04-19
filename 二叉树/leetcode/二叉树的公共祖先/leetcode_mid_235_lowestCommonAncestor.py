
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.p = p
        self.q = q

        def dfs(node):
            if not node:
                return
            
            if node.val > self.p.val and node.val > self.q.val:
                return dfs(node.left)
            
            if node.val < self.p.val and node.val < self.q.val:
                return dfs(node.right)
            
            return node
        
        return dfs(root)




class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root