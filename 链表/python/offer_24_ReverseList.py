# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路： 建立一个新的头结点，然后遍历链表，采用头插法将所有节点插入到新链表中

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here

        new_head = ListNode(0)
        while pHead:
            next_node = pHead.next
            pHead.next = new_head.next
            new_head.next = pHead
            
            pHead = next_node
        return new_head.next

