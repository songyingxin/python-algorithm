
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.head = None

        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            dfs(node.left)
            node.left = None
            node.right = self.head
            self.head = node
        
        dfs(root)

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        stack = [root]

        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if stack != []:
                node.left = None
                node.right = stack[-1]