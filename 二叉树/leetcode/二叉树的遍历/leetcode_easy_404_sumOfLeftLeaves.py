
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        def dfs(node):
            if not node:
                return
            
            if node.left and not node.left.left and not node.left.right:
                    self.res += node.left.val
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.res

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        if root and root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    