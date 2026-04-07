class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        pos = len(nums) - 1

        while left <= right:

            left_val = nums[left] * nums[left]
            right_val = nums[right] * nums[right]

            if left_val > right_val:
                res[pos] = left_val
                pos -= 1
                left += 1
            else:
                res[pos] = right_val
                pos -= 1
                right -= 1
        
        return res