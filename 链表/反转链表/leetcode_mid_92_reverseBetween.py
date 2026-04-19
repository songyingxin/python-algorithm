# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head, left, right):

        new_head = ListNode(0)
        new_head.next = head

        pre = new_head  # 第一个反转节点的前驱节点

        for i  in range(left-1):
            pre = pre.next
        
        head = pre.next  # 第一个要反转的节点

        for i in range(right-left):  # 从第二个要反转的节点采用头插法插入
            next_node = head.next
            head.next = next_node.next
            next_node.next = pre.next
            pre.next = next_node
        
        return new_head.next






        
