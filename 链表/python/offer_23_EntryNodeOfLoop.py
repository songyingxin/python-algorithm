# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next or not pHead.next.next:
            return None

        slow = pHead.next
        fast = slow.next

        while slow != fast:
            if not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next
        
        fast = pHead
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow


