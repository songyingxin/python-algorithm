

# 


# 思路：
# - 如何判断链表是否有环：快慢指针法，分别定义fast和slow指针，从头结点出发，fast指针每次移动两个节点，slow指针每次移动一个节点，如果fast和slow指针相遇，则说明有环
# - 如何找到环的入口：相遇后，快指针回到头结点，然后快慢指针每次移动一个节点，直到两个指针相遇
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head

        while slow and fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if slow == fast:
                break
        if not slow or not fast:
            return 
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
        
        

