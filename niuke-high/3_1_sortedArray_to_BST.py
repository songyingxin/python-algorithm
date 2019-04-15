# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        return self.BTS(nums, 0, len(nums) - 1)
        
    
    def BTS(self, nums, start, end):
        if start > end:
            return None
       
        mid = (start + end) // 2
        head = TreeNode(nums[mid])
        head.left = self.BTS(nums, start, mid - 1)
        head.right = self.BTS(nums, mid+1, end)

        return head
