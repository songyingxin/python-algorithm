class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_head = ListNode()
        node = new_head

        while head and head.next:
            fir_node = head
            sec_node = head.next

            head = head.next.next

            fir_node.next = node.next
            node.next = sec_node
            sec_node.next = fir_node

            node = node.next.next
        
        if head:
            node.next = head
        
        return new_head.next