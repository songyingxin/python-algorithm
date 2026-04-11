
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        nums = [num*num for num in nums]

        left = 0
        right = len(nums) - 1

        new_nums = []
        while left <= right:
            if nums[left] > nums[right]:
                new_nums.append(nums[left])
                left += 1
            else:
                new_nums.append(nums[right])
                right -= 1
        
        return new_nums[::-1]



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