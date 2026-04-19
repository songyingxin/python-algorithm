class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        self.val = val

        def dfs(node):
            if not node:
                return TreeNode(self.val)
            
            if node.val < self.val:
                node.right = dfs(node.right)
            else:
                node.left = dfs(node.left)
            
            return node
        
        return dfs(root)


# 迭代法
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        
        now_node = TreeNode(val)

        node = root
        while node:
            if val < node.val:
                if not node.left:
                    node.left = now_node
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = now_node
                    break
                else:
                    node = node.right

        return root    