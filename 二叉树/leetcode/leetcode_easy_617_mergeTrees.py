


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return
        
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        node = TreeNode(root1.val + root2.val)

        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)

        return node
        