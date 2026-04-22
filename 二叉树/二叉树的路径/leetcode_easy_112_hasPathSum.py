
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, target):
            if not node:
                return False 

            target -= node.val
            if not node.left and not node.right:
                return target == 0
            
            left = dfs(node.left, target)
            right = dfs(node.right, target)
            return left or right
        
        return dfs(root, targetSum)


class Solution:
    def hasPathSum(self, root, sum):

        if not root:
            return False

        # 终止条件： 该节点是否为叶子节点
        if not root.left and not root.right:
            return sum == root.val

        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
