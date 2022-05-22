# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def KthNode(self , proot: TreeNode, k: int) -> int:
        # write code here
        array = []
        def inorder(proot):
            if not proot:
                return None
            inorder(proot.left)
            array.append(proot.val)
            inorder(proot.right)
            
        if not proot or k == 0:
            return -1

        inorder(proot)
        
        if len(array) < k:
            return -1
        
        return array[k-1]



