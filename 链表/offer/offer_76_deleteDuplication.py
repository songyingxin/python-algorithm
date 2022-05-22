


class Solution:
    def deleteDuplication(self , pHead: ListNode) -> ListNode:
        # write code here
        new_head = ListNode(-1)
        node = new_head
        while pHead:
            if pHead.next == None or pHead.next.val != pHead.val:
                node.next = pHead
                node = pHead
            while pHead.next != None and pHead.val == pHead.next.val:
                pHead = pHead.next
            pHead = pHead.next
        node.next = None
        return new_head.next