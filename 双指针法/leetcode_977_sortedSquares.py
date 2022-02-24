

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left = 0
        right = len(nums) - 1

        res = []
        while left <= right:
            left_val = nums[left] ** 2
            right_val = nums[right] ** 2
            if left_val > right_val:
                res.append(left_val)
                left += 1
            else:
                res.append(right_val)
                right -= 1
        
        return res[::-1]