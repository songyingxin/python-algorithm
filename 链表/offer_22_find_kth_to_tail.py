# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here

        pre_ptr = head

        while k != 0 and pre_ptr:
            pre_ptr = pre_ptr.next
            k -= 1
        
        if k != 0:
            return None
        
        while pre_ptr:
            pre_ptr = pre_ptr.next
            head = head.next
        
        return head

