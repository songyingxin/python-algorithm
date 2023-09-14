class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_num = nums[0]
        pre = 0
        for num in nums:
            now = max(num, pre+num)
            max_num = max(now, max_num)
            pre = now
        
        return max_num
            