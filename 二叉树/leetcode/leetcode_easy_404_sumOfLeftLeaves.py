class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        if root and root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    
