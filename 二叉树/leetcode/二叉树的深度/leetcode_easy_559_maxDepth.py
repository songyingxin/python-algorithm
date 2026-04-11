class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def dfs(node):
            if not node:
                return 0

            depth = 0
            for child in node.children:
                child_depth = dfs(child)
                depth = max(depth, child_depth)

            return depth + 1
        
        return dfs(root)