# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.is_mirror(root.left, root.right)

    
    def is_mirror(self, p, q):

        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        l = self.is_mirror(p.left, q.right)
        r = self.is_mirror(p.right, q.left)

        return p.val == q.val and l and r
