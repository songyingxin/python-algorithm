# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 不偷 root 节点
        not_rob = 0
        if root.left:
            not_rob += self.rob(root.left) 
        if root.right:
            not_rob += self.rob(root.right)

        # 偷 root 节点
        rob_root = root.val
        if root.left and root.left.left:
            rob_root += self.rob(root.left.left)
        
        if root.left and root.left.right:
            rob_root += self.rob(root.left.right)
        
        if root.right and root.right.left:
            rob_root += self.rob(root.right.left)

        if root.right and root.right.right:
            rob_root += self.rob(root.right.right)
        
        return max(rob_root, not_rob)


# dp
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))
    

    def dp(self, cur):
        """
        返回值：
            dp[0]: 不 rob 根节点值的最大值
            dp[1]: rob 根节点的最大值
        """
        if not cur:
            return [0, 0]
        l = self.dp(cur.left)
        r = self.dp(cur.right)

        return [max(l) + max(r), cur.val + l[0] + r[0]]
