# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        new_head = ListNode(0)
        p_node = new_head
        is_up = 0

        while l1 and l2:

            new_val = l1.val + l2.val + is_up
            node = ListNode(new_val%10)
            is_up = new_val // 10

            node.next = p_node.next
            p_node.next = node
            
            p_node = p_node.next

            l1 = l1.next
            l2 = l2.next
        
        other = l1 if l1 else l2

        while other:
            new_val = other.val + is_up
            node = ListNode(new_val % 10)
            is_up = new_val // 10

            node.next = p_node.next
            p_node.next = node

            p_node = p_node.next
            
            other = other.next
        
        if is_up != 0:
            node = ListNode(is_up)
            node.next = p_node.next
            p_node.next = node

        return new_head.next



            





