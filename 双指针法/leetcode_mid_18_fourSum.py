class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)
        n = len(nums)

        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                sum_i_j = nums[i] + nums[j]

                left = j + 1
                right = n - 1

                while left < right:
                    if left > j+1 and nums[left] == nums[left-1]:
                        left += 1
                        continue

                    sum_val = sum_i_j + nums[left] + nums[right]

                    if sum_val == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                    elif sum_val < target:
                        left += 1
                    else:
                        right -= 1
        
        return res