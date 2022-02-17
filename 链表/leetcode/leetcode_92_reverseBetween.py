# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head, m, n):

        new_head = ListNode(0)
        new_head.next = head

        pre = new_head  # 第一个反转节点的前驱节点

        for i  in range(m-1):
            pre = pre.next
        
        head = pre.next  # 第一个要反转的节点

        for i in range( n - m):  # 从第二个要反转的节点采用头插法插入
            next_ptr = head.next
            head.next = next_ptr.next
            next_ptr.next = pre.next
            pre.next = next_ptr
        
        return new_head.next






        
