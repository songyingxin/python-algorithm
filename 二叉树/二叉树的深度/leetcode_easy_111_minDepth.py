


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            
            if not node.left:
                return dfs(node.right) + 1

            if not node.right:
                return dfs(node.right) + 1
            
            left = dfs(node.left) 
            right = dfs(node.right)

            return min(left,right) + 1
        
        return dfs(root)
    

class Solution:
    def minDepth(self, root):

        if not root:
            return 0
        
        if not root.left:
            return self.minDepth(root.right) + 1
        
        if not root.right:
            return self.minDepth(root.left) + 1
        
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

