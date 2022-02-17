class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        new_head = ListNode(-1)
        new_head.next = head
        node = new_head

        while node.next and node.next.next:
            a, b = node.next, node.next.next
            node.next, a.next = b, b.next
            b.next = a
            node = node.next.next
        
        return new_head.next
