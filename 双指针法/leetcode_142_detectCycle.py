

# 


# 思路：
# - 如何判断链表是否有环：快慢指针法，分别定义fast和slow指针，从头结点出发，fast指针每次移动两个节点，slow指针每次移动一个节点，如果fast和slow指针相遇，则说明有环
# - 如何找到环的入口：相遇后，快指针回到头结点，然后快慢指针每次移动一个节点，直到两个指针相遇

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fast_ptr = slow_ptr = head
        has_cycle = False

        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                has_cycle = True
                break

        if not has_cycle:
            return None

        fast_ptr = head

        while fast_ptr and slow_ptr:
            if fast_ptr == slow_ptr:
                return fast_ptr
            
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        
        

