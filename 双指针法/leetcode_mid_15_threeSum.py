class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        nums_len = len(nums)

        res = []
        for i in range(nums_len):

            # 提前退出
            if nums[i] > 0:
                return res

            # 去重
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = nums_len-1

            sub_val = 0-nums[i]
            while left < right:
                # 提前退出
                if nums[left] > sub_val:
                    break
                
                # 去重
                if left > i+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                
                sum_val = nums[left] + nums[right]
                if sum_val == sub_val:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif sum_val > sub_val:
                    right -= 1
                else:
                    left += 1
        
        return res