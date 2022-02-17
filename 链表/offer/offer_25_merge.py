# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 新建一个头节点，哪个小取哪个， 最后把非空的接在新链表后面

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here

        new_head = ListNode(0)
        node = new_head

        while pHead1 and pHead2:

            if pHead1.val < pHead2.val:
                node.next = pHead1
                pHead1 = pHead1.next
            else:
                node.next = pHead2
                pHead2 = pHead2.next

            node = node.next

        if pHead1:
            node.next = pHead1
        elif pHead2:
            node.next = pHead2
        
        return new_head.next
