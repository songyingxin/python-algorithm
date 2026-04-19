# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head

        while fast and slow:
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            
            fast = fast.next
            if slow == fast:
                return True
        
        return False

