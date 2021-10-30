# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路： 快慢指针。 快指针一次走两步，慢指针一次走一步，同时出发，在第一次相遇后，快指针回到起点，一次走一步，二者最终相遇的点就是环的入口节点。
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


