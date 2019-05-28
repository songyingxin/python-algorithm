# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        new_head = ListNode(0)
        new_head.next = None
        pre_ptr = new_head

        while l1 and l2:

            if l1.val < l2.val:
                next_l1 = l1.next
                l1.next = pre_ptr.next
                pre_ptr.next = l1
                pre_ptr = l1
                l1 = next_l1
            else:
                next_l2 = l2.next
                l2.next = pre_ptr.next
                pre_ptr.next = l2
                pre_ptr = l2
                l2 = next_l2
        
        while l1:
            next_l1 = l1.next
            l1.next = pre_ptr.next
            pre_ptr.next = l1
            pre_ptr = l1
            l1 = next_l1
        while l2:
            next_l2 = l2.next
            l2.next = pre_ptr.next
            pre_ptr.next = l2
            pre_ptr = l2
            l2 = next_l2
        
        return new_head.next


        
