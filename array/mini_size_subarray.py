# -*- coding:utf-8 -*-


class Solution_high:
    """ 思路2: 不定窗口滑动 """
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        left, right  = 0, -1  # nums[left...right] 为我们的滑动窗口
        sum = 0
        res = len(nums) + 1

        while left < len(nums):
            if right + 1 < len(nums) and sum < s:
                right += 1
                sum += nums[right]
            else:
                sum -= nums[left]
                left -= 1

            if (sum >= s):
                res = min(res, r-l+1)
            
        if res == len(nums) + 1:
            return 0
            
        return res

