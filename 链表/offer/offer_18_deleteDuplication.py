# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：维护两个指针： res 指向新链表的最后一个元素， tmp 用来遍历链表， 在遍历过程中，找到下一个不重复的节点，插入到 res 后面。判断方法直接采用当前节点的值与下一节点的值是否相同。 考虑到头节点也有可能被删除，因此建立一个新的头节点更容易处理。

class Solution:
    def deleteNode(self , head: ListNode, val: int):
        # write code here

        result = ListNode(0)
        pre_node = result 
        result.next = head

        while head and head.next:
            if head.val == val:
                while head.next and head.val == head.next.val:
                    head = head.next
            else:
                pre_node.next = head
                pre_node = pre_node.next
            
            head = head.next
        pre_node.next = head
        return result.next





