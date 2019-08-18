# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.res.append(root.val)

        return self.res


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
            
            res.append(node.val)
        
        return res[::-1]
