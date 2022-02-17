# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路1: 空间复杂度O(n)，时间复杂度O(n) 采用一个列表保存链表所有节点，然后直接返回倒序数组。
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]

    def printListFromTailToHead(self, listNode):
        # write code here
        arr = []
        while(listNode):
            arr.append(listNode.val)
            listNode = listNode.next

        return arr[::-1]


# 思路2： 空间复杂度O(n)，时间复杂度O(n) 采用递归的思想来做。
# 由于链表长度可能非常长，会导致函数调用层级很深，可能导致函数调用栈溢出，因此此例子牛客现在无法通过，
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        result =[]

        def dfs(listNode):
            if not listNode:
                return 
            
            dfs(listNode.next)
            result.append(listNode.val)
        dfs(listNode)
        return result
