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


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        head_a = headA
        head_b = headB

        headA_len = 0
        headB_len = 0

        while headA:
            headA_len += 1
            headA = headA.next
        
        while headB:
            headB_len += 1
            headB = headB.next
        
        if headA_len > headB_len:
            for i in range(headA_len - headB_len):
                head_a = head_a.next
        else:
            for i in range(headB_len - headA_len):
                head_b = head_b.next
        
        while head_a and head_b:

            if head_a == head_b:
                return head_a
            else:
                head_a = head_a.next
                head_b = head_b.next
        
        return None

