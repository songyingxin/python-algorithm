
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dele_num = set()

        pre_val = None
        node = head
        while node:
            if node.val == pre_val:
                dele_num.add(node.val)
            pre_val = node.val
            node = node.next
        
        new_head = ListNode()
        node = new_head
        while head:
            if head.val in dele_num:
                head = head.next
            else:
                next_node = head.next
                head.next = node.next
                node.next = head 
                node = node.next
                head = next_node
        
        return new_head.next






class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        new_head = ListNode(None)
        new_head.next = head

        cur = new_head

        while cur and cur.next:
            begin = cur.next
            if begin.next and begin.val == begin.next.val:
                end = begin.next
                while end.next and end.val == end.next.val:
                    end = end.next

                cur.next = end.next
            else:
                cur = cur.next

        return new_head.next
