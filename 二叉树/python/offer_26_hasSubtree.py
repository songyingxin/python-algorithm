# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here

        if not pRoot1 or not pRoot2:
            return False
        
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

        
    def is_subtree(self, A, B):
        """
        判断树  B 是否为 树 A 的子树， 树A 的头 == 树 B 的头
        """
        if not B:
            return True
        
        if not A or A.val != B.val:
            return False
        
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)




