# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fast_ptr = slow_ptr = head
        has_cycle = False

        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                has_cycle = True
                break

        if not has_cycle:
            return None

        fast_ptr = head

        while fast_ptr and slow_ptr:
            if fast_ptr == slow_ptr:
                return fast_ptr
            
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        
        

