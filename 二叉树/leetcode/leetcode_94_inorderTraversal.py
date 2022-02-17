# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归


class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return 
        
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)

        return self.res

# 迭代
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        res = []
        p = root

        while p or stack:

            # 先把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            tmp = stack.pop()
            res.append(tmp.val)
            p = tmp.right
        
        return res





