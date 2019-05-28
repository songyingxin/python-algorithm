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
            return head
        
        node = head
        map_node = {}

        while node:
            clone = Node(node.val, None, None)
            map_node[node] = clone
            node = node.next
        
        node = head
        while node:
            if node.next:
                map_node[node].next = map_node[node.next]
            else:
                map_node[node].next = None
            
            if node.random:
                map_node[node].random = map_node[node.random]
            else:
                map_node[node].random = None

            node = node.next
        
        return map_node[head]




