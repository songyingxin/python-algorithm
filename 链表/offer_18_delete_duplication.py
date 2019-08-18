# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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





