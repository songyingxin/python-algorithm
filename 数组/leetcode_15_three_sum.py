class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        target = 0
        nums = sorted(nums)
        pre_val = None

        for i in range(len(nums)):

            if nums[i] == pre_val:
                continue
            pre_val = nums[i]

            res = self.two_sum(nums[i+1:], target- nums[i])
            for val in res:
                result.append([nums[i], val[0], val[1]])
            
        return result

    def two_sum(self, nums, target):
        
        res = []

        pre_left_val = None
        pre_right_val = None

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] == pre_left_val:
                left += 1
                continue
            
            if nums[right] == pre_right_val:
                right -= 1
                continue

            if nums[left] + nums[right] == target:
                res.append([nums[left], nums[right]])

                pre_left_val = nums[left]
                left += 1
            
            if nums[left] + nums[right] > target:
                pre_right_val = nums[right]
                right -= 1
            
            if nums[left] + nums[right] < target:
                pre_left_val = nums[left]
                left += 1
        
        return res



