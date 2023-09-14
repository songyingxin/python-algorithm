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

            if list1.val < list2.val:
                next_node = list1.next
                list1.next = node.next
                node.next = list1

                list1 = next_node
                node = node.next
            else:
                next_node = list2.next
                list2.next = node.next
                node.next = list2

                list2 = next_node
                node = node.next
        
        tmp_list = list1 if list1 else list2

        node.next = tmp_list
        return new_head.next


        
