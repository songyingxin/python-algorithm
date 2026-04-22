
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return res

# 迭代
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []

        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            tmp = stack.pop()
            res.append(tmp.val)
            node = tmp.right
        
        return res





