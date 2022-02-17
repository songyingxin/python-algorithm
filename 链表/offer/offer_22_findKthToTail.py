# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路： 设定一个指针，让该指针先走 k 步， 然后 两个指针一直走，直到第一个指针走到头。
# 需要注意处理空 head 的情况
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        
        slow = head
        while k > 0:
            if not slow:
                return None
            k -= 1
            slow = slow.next

        while slow:
            head = head.next
            slow = slow.next
        
        return head

