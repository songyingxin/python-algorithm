class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        left = 0
        right = 0
        sum_val = nums[0]

        min_arr_len = float('inf')

        while right < n:
            if sum_val < target:
                right += 1
                if right<n:
                    sum_val += nums[right]
            else:
                now_len = right-left+1
                min_arr_len = min(min_arr_len, now_len)
                sum_val -= nums[left]
                left += 1
                
        
        if min_arr_len == float('inf'):
            return 0
        else:
            return min_arr_len
