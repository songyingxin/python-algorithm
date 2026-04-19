"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return
        
        node = head

        # key:原节点， value：复制出来的新节点
        map_node = {}
        while node:
            clone = Node(node.val, None, None)
            map_node[node] = clone
            node = node.next
        
        node = head
        while node:
            # 克隆 next 指针
            if node.next:
                map_node[node].next = map_node[node.next]
            
            # 克隆 random 指针
            if node.random:
                map_node[node].random = map_node[node.random]

            node = node.next
        
        return map_node[head]




