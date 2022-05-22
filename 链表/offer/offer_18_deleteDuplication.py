# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self , head: ListNode, val: int):
        # write code here

        new_head = ListNode(0)
        node = new_head
        
        while head:
            if head.val != val:
                next_node = head.next
                head.next = node.next
                node.next = head
                
                node = node.next
                head = next_node 
            else:
                head = head.next
        return new_head.next





