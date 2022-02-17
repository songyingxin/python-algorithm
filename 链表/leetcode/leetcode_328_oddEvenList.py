

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        odd = ListNode(0)
        odd_node = odd

        even = ListNode(0)
        even_node = even

        flag = True

        while head:
            tmp = head.next
            if flag:
                head.next = odd_node.next
                odd_node.next = head

                odd_node = odd_node.next
                flag = False
            else:
                head.next = even_node.next
                even_node.next = head

                even_node = even_node.next
                flag = True
            head = tmp

        odd_node.next = even.next
        return odd.next
