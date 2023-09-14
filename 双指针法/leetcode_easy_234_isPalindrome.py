# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        reverse_list = []

        node = head
        while node:
            reverse_list.append(node.val)
            node = node.next
        
        for i in range(len(reverse_list) // 2):
            if head.val == reverse_list[-i-1]:
                head = head.next
            else:
                return False
            
        return True







