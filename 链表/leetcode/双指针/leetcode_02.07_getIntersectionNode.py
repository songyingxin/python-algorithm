# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        headA_len = 0
        headB_len = 0
        node = headA
        while node:
            node = node.next
            headA_len += 1
        
        node = headB
        while node:
            node = node.next
            headB_len += 1
        
        if headB_len > headA_len:
            for i in range(headB_len-headA_len):
                headB = headB.next
        else:
            for i in range(headA_len-headB_len):
                headA = headA.next
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None