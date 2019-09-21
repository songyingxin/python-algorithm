# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        new_head = ListNode(None)
        node = new_head

        while head:
            if head.val == node.val:
                head = head.next
                continue
            else:
                tmp = head.next
                head.next = node.next
                node.next = head

                node = head
                head = tmp

        return new_head.next
