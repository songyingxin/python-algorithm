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
