


class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code here
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == sum
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)