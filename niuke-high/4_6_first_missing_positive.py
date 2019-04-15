class Solution:
    def firstMissingPositive(self, nums) :

        start = 0  
        end = len(nums) # 如果全存在时的最大的数

        while start < end:

            if nums[start] == start +1:
                start += 1
            elif nums[start] <= start or nums[start] > end or nums[nums[start]-1] == nums[start]:
                end -= 1
                nums[start] = nums[end]
            else:
                print(nums)
                tmp = nums[start]
                nums[start]=  nums[nums[start] - 1]
                nums[tmp-1] = tmp
                print(nums)

        return start + 1

nums = [7, 8, 9, 11, 12]
nums = [3, 4, -1, 1]
# nums = [1, 2, 0]
nums = [0, 1, 2]
print(Solution().firstMissingPositive(nums))

