# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here

        if not pHead:
            return None

        slow_ptr = pHead.next

        if slow_ptr:
            fast_ptr = slow_ptr.next
        else:
            return None

        while slow_ptr != fast_ptr and fast_ptr:

            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
            if not fast_ptr:
                return None
            fast_ptr = fast_ptr.next
        
        if not fast_ptr:
            return None
        
        fast_ptr = pHead

        while slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        
        return slow_ptr


