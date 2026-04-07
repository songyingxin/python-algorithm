# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        add_num = 0
        new_head = ListNode(0)
        node = new_head

        while l1 and l2:
            val = l1.val + l2.val + add_num

            node.next = ListNode(val % 10)
            node = node.next

            add_num = val // 10

            l1 = l1.next
            l2 = l2.next

        
        l = l1 if l1 else l2
        
        while l:
            val = l.val + add_num
            node.next = ListNode(val % 10)
            node = node.next

            add_num = val // 10
            
            l = l.next

        if add_num == 1:
            node.next = ListNode(1)

        return new_head.next



            





