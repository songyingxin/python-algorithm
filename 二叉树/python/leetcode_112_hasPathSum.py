class Solution:
    def hasPathSum(self, root, sum):

        if not root:
            return False

        # 终止条件： 该节点是否为叶子节点
        if not root.left and not root.right:
            return sum == root.val

        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
