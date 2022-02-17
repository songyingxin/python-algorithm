# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        self.arr = []
        if k == 0 or pRoot == None:
            return None
        self._inorder_traversal(pRoot)

        if  k > len(self.arr):
            return None

        return self.arr[k-1]

    def _inorder_traversal(self, root):

        if root.left:
            self._inorder_traversal(root.left)
        
        self.arr.append(root)

        if root.right:
            self._inorder_traversal(root.right)



