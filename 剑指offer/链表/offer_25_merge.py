# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 新建一个头节点，哪个小取哪个， 最后把非空的接在新链表后面

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        node = new_head
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        
        elif l2:
            node.next = l2
        
        return new_head.next
