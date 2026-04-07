# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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
