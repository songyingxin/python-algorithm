# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        is_up = 0
        new_head = ListNode(0)
        node = new_head

        while l1 and l2:
            now_val = l1.val + l2.val + is_up
            is_up = now_val // 10
            now_node = ListNode(now_val % 10)

            now_node.next = node.next
            node.next = now_node
            node = now_node

            l1 = l1.next
            l2 = l2.next
        
        list_node = l1 if l1 else l2
        while list_node:
            now_val = list_node.val + is_up
            is_up = now_val // 10
            now_node = ListNode(now_val % 10)

            now_node.next = node.next
            node.next = now_node
            node = now_node

            list_node = list_node.next
        
        if is_up != 0:
            now_node = ListNode(is_up)
            now_node.next = node.next
            node.next = now_node
        
        return new_head.next



            





