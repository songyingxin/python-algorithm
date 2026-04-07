class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def dfs(node):
            if not node:
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res



# 迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root:
            return res
        
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res

