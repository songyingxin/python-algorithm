class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_head = ListNode(0)

        node = new_head

        while head and head.next:
            head_next = head.next
            next_node = head_next.next

            head_next.next = head
            head.next = node.next
            node.next = head_next

            node = node.next.next
            head = next_node
        
        if head:
            head.next = node.next
            node.next = head
        
        return new_head.next
