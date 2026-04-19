# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        l_head = ListNode()
        h_head = ListNode()

        l_node = l_head
        h_node = h_head

        while head:
            next_node = head.next
            if head.val < x:
                head.next = l_node.next
                l_node.next = head
                l_node = l_node.next
            else:
                head.next = h_node.next
                h_node.next = head
                h_node = h_node.next
            
            head = next_node

        l_node.next = h_head.next
        return l_head.next


        
