
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
        
        cut_len = abs(headA_len-headB_len)

        if headA_len > headB_len:
            while cut_len > 0:
                headA = headA.next
                cut_len -= 1
        else:
            while cut_len > 0:
                headB = headB.next
                cut_len -= 1
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return 
