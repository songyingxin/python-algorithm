# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here

        if not pNode:
            return pNode

        # 该节点有右子树， 找右子树的最左节点
        if pNode.right:
            start = pNode.right

            while start.left:
                start = start.left

            return start

        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp

            pNode = tmp
