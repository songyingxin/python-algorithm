# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 首先分别遍历两个链表，得到两个链表的长度 length1， length2， 然后让较长的链表先走 length - length2 步， 然后再一起走
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here

        node1 = pHead1
        node2 = pHead2
        length1 = 0
        length2 = 0

        while node1:
            length1 += 1
            node1 = node1.next

        while node2:
            length2 += 1
            node2 = node2.next

        distance = abs(length1 - length2)
        if length1 > length2:
            while distance > 0:
                pHead1 = pHead1.next
                distance -= 1
        else:
            while distance > 0:
                pHead2 = pHead2.next
                distance -= 1

        while pHead1 and pHead2:
            if pHead1.val == pHead2.val:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        return None
