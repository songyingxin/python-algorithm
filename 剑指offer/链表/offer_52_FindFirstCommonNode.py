# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 首先分别遍历两个链表，得到两个链表的长度 length1， length2， 然后让较长的链表先走 length - length2 步， 然后再一起走
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        
        return nodeA
