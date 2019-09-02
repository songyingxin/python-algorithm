# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路1
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]

    def printListFromTailToHead(self, listNode):
        # write code here
        arr = []
        while(listNode):
            arr.append(listNode.val)
            listNode = listNode.next

        return arr[::-1]


# 思路2： 递归
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        result =[]

        def recu(listNode):
            if not listNode:
                return 
            
            recu(listNode.next)
            result.append(listNode.val)
        recu(listNode)
        return result
