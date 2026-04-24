# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# dp
class Solution:
    def rob(self, root: TreeNode) -> int:

        def dfs(node):
            """
            返回值：
                max_not_has_node: 不 rob 根节点值的最大值
                max_has_node: rob 根节点的最大值
            """
            if not node:
                return [0,0]
            l = dfs(node.left)
            r = dfs(node.right)

            max_not_has_node = max(l) + max(r)
            max_has_node = node.val + l[0] + r[0]
            return [max_not_has_node, max_has_node]

        root_max_val = dfs(root)
        return max(root_max_val)
    
