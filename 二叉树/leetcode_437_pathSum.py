# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        return self.path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def path(self, root, sum):
        if not root:
            return 0
        
        sum -= root.val

        if sum == 0:
            return 1 + self.path(root.left, sum) + self.path(root.right, sum)
        else:
            return 0 + self.path(root.left, sum) + self.path(root.right, sum)



    





