# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 空间复杂度 O(N)
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        def deserialize(l):
            if l[0] == '#':
                l.pop(0)
                return None

            root = TreeNode(int(l[0]))
            l.pop(0)
            root.left = deserialize(l)
            root.right = deserialize(l)
            return root
        
        data_list = s.split(',')
        root = deserialize(data_list)
        return root
