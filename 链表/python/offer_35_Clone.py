# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# 递归思路
class Solution:
    # 返回 RandomListNode
    def __init__(self):
        self.visited = {}

    def get_clone_node(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = RandomListNode(node.label)
                return self.visited[node]
        return None

    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        
        old_node = pHead
        new_node = RandomListNode(old_node.label)

        self.visited[old_node] = new_node

        while old_node:
            new_node.random = self.get_clone_node(old_node.random)
            new_node.next = self.get_clone_node(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        
        return self.visited[pHead]


        