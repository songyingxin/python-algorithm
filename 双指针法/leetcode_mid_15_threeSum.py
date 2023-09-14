class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target_val = 0 - nums[i]

            left = i+1
            right = len(nums) - 1

            while left < right:
                if left > i+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue

                now_val = nums[left] + nums[right]

                if now_val == target_val:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif now_val < target_val:
                    left += 1
                else:
                    right -= 1
        
        return res