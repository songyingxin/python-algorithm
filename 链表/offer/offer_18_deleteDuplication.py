# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：维护两个指针： res 指向新链表的最后一个元素， tmp 用来遍历链表， 在遍历过程中，找到下一个不重复的节点，插入到 res 后面。判断方法直接采用当前节点的值与下一节点的值是否相同。 考虑到头节点也有可能被删除，因此建立一个新的头节点更容易处理。

class Solution:
    def deleteDuplication(self, pHead):
        # write code here

        result = ListNode(0)
        res = result 
        result.next = pHead

        tmp = pHead

        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                while tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
            else:
                res.next = tmp
                res = res.next
            
            tmp = tmp.next
        res.next = tmp
        return result.next





