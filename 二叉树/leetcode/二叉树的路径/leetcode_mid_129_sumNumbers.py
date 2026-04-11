
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(node,node_sum):
            if not node:
                return
            
            node_sum = node_sum*10 + node.val
            if not node.left and not node.right:
                self.res += node_sum
                return
            
            dfs(node.left, node_sum)
            dfs(node.right,node_sum)
        
        dfs(root,0)
        return self.res
