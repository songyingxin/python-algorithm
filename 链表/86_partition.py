# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        low_head = ListNode(0)
        low_head.next = None
        pre_low = low_head

        high_head = ListNode(0)
        high_head.next = None
        pre_high = high_head

        while head:
            next_ptr = head.next
            if head.val < x:
                head.next = pre_low.next
                pre_low.next = head
                pre_low = head
            else:
                head.next = pre_high.next
                pre_high.next = head
                pre_high = head
            
            head = next_ptr
        
        pre_low.next = high_head.next

        return low_head.next


        
