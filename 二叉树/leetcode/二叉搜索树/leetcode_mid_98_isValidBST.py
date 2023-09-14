class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

      self.pre_val = float('-inf')

      def dfs(node):
        if not node:
          return True
        
        left = dfs(node.left)
        if not left:
          return False
        
        if node.val <= self.pre_val:
          return False

        self.pre_val = node.val
        right = dfs(node.right)

        return right
      
      return dfs(root)

        
    


