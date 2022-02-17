# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

#   - 如果一个结点有**右子树**，则它的下一个结点就是**它的右子树中的最左子结点**； 
#   - 如果**没有右子树**，且其为其父节点的**左子结点**， 则它的下一个结点就是它的父结点
#   - 如果**没有右子树**， 且它为它父节点的**右子结点**， 则我们需要沿着指向父节点的指针一直向上遍历，直到找到一个它是该父节点的左子结点。此时，该父节点就是我们要找的下一个结点。
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
        
        # 该节点无右子树，且其为父节点的左子节点 
        if not pNode.right and pNode.next and pNode.next.left == pNode:
            return pNode.next

        # 该节点无右子树，找到
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp

            pNode = tmp
