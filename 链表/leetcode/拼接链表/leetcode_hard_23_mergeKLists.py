# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if len(lists) == 2:
            return self.merge_two_list(lists[0], lists[1])
        
        if len(lists) == 1:
            return lists[0]

        if not lists:
            return None
        
        mid = len(lists) // 2
        left_lists = lists[:mid]
        right_lists = lists[mid:]

        left_head = self.mergeKLists(left_lists)
        right_head = self.mergeKLists(right_lists)

        return self.merge_two_list(left_head, right_head)


    def merge_two_list(self, l1, l2):
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
