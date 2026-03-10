# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        all = set()

        while headA != None:
            all.add(headA)
            headA = headA.next
        
        while headB != None:
            if headB in all:
                return headB
            headB = headB.next
        
        return None



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

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
        
        abs_len = abs(headA_len-headB_len)
        if headA_len > headB_len:
            while abs_len > 0:
                headA = headA.next
                abs_len -= 1
        else:
            while abs_len > 0:
                headB = headB.next
                abs_len -= 1
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None





