
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        new_head = ListNode(0)
        node = new_head

        while head:
            tmp = head.next
            if head.val != val:
                head.next = node.next
                node.next = head

                node = node.next
            head = tmp

        return new_head.next
