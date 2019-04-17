# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路1
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)

        node = head
        while node:
            next_node = node.next
            node.next = new_head.next
            new_head.next = node
            node = next_node

        return new_head.next

# 思路2
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None

        while head:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node

        return new_head
