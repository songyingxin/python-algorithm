class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        left, right = 0, n-1
        
        # 找左边界：第一个逆序的位置
        while left < n-1 and nums[left] <= nums[left+1]:
            left += 1

        # 说明有序，直接返回0
        if left == n-1:
            return 0
        
        # 找右边界：最后一个逆序的位置
        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1
        
        # 针对中间的num，要重新确定左右边界
        sub = nums[left:right+1]
        while left > 0 and nums[left-1] > min(sub):
            left -= 1
        while right < n-1 and nums[right+1] < max(sub):
            right += 1
            
        return right - left + 1
        
