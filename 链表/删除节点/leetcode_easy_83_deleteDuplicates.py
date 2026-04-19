# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_head = ListNode(None)

        node = new_head

        while head:
            if node.val == head.val:
                head = head.next
            else:
                next_node = head.next
                head.next = node.next
                node.next = head
                node = node.next
                
                head = next_node
        
        return new_head.next
