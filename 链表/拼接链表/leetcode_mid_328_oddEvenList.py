class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd_head = ListNode()
        even_head = ListNode()

        odd_node = odd_head
        even_node = even_head

        while head and head.next:
            
            fir_node = head
            sec_node = head.next

            head = sec_node.next

            fir_node.next = odd_node.next
            odd_node.next = fir_node
            odd_node = odd_node.next

            sec_node.next = even_node.next
            even_node.next = sec_node
            even_node = even_node.next

        if head:
            odd_node.next = head
            odd_node = odd_node.next
        
        odd_node.next = even_head.next
        return odd_head.next
