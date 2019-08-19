# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next

        while fast and fast.next:
            fast, slow = fast.next.next , slow.next
        
        mid, slow.next = slow.next, None

        left, right = self.sortList(head), self.sortList(mid)

        h = res = ListNode(0)

        while left and right:
            if left.val < right.val :
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        
        h.next = left if left else right

        return res.next



