# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归


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
        return  res

# 迭代
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        res = []
        p = root

        while p and stack:

            # 先把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            tmp = stack.pop()
            res.append(tmp.val)
            p = tmp.right
        
        return res





