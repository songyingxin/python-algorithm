class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def dfs(node):
            if not node:
                return 0
            
            max_len = 0
            for child in node.children:
                max_len = max(max_len, dfs(child))
            
            return max_len + 1
        
        return dfs(root)