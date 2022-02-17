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

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return 
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.res



# 迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root:
            return res
        
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res

