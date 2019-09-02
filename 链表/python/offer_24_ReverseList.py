# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here

        if not pHead or not pHead.next:
            return pHead
        
        new_head = ListNode(0)
        
        while pHead:

            tmp = pHead.next

            pHead.next = new_head.next
            new_head.next = pHead

            pHead = tmp
        
        return new_head.next

