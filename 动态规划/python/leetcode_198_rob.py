class Solution:
    def rob(self, nums: List[int]) -> int:

        prev_max = 0
        curr_max = 0

        for val in nums:
            prev_max, curr_max = curr_max, max(prev_max + val, curr_max)

        return curr_max
