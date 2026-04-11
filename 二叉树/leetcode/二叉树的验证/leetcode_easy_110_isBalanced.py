
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            return max(left,right) + 1
        
        if not root:
            return True
        
        left_depth = dfs(root.left)
        right_depth = dfs(root.right)

        if abs(left_depth-right_depth) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0, True
            left_depth,left = dfs(node.left)
            right_depth,right = dfs(node.right)

            depth = max(left_depth, right_depth) + 1
            if left and right and abs(left_depth-right_depth) < 2:
                return depth,True
            else:
                return depth,False
        
        depth, balance = dfs(root)
        return balance