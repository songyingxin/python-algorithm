class Solution:
    def threeSum(self, nums):
        result = []
        target = 0
        nums = sorted(nums)
        pre_num = None
        for i in range(len(nums)):
            if nums[i] == pre_num:
                continue
            pre_num = nums[i]
            sub_num = target - nums[i]
            pre_left = None
            pre_right = None
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] == pre_left:
                    left += 1
                    continue
                
                if nums[right] == pre_right:
                    right -= 1
                    continue
                
                if nums[left] + nums[right] ==  sub_num:
                    result.append([nums[i], nums[left], nums[right]])
                    pre_left = nums[left]
                    left += 1
                elif nums[left] + nums[right] > sub_num:
                    pre_right = nums[right]
                    right -= 1
                else:
                    pre_left = nums[left]
                    left += 1
        return result


nums = [0, 0, 0, 0]
print(Solution().threeSum(nums))



