# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_head = ListNode(0)
        node = new_head

        while list1 and list2:

            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 if list1 else list2
        return new_head.next


        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_head = ListNode()

        node = new_head

        while list1 and list2:
            if list1.val < list2.val:
                next_node = list1.next
                list1.next = node.next
                node.next = list1
                node = node.next
                list1 = next_node
            else:
                next_node = list2.next
                list2.next = node.next
                node.next = list2
                node = node.next
                list2 = next_node
        
        if list1:
            node.next = list1
        else:
            node.next = list2

        return new_head.next