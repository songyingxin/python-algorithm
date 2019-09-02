# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路1
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)

        while head:
            next_node = head.next    # 临时保存下一个节点

            # 将 head 插入到 new_head 中
            head.next = new_head.next  
            new_head.next = head

            # 迁移下一个节点
            head = next_node

        return new_head.next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return p
        
