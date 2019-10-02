
# 思路1 
class Solution:
    def twoSum(self, nums, target):

        sorted_id = sorted(range(len(nums)), key=lambda k:nums[k])  # 对下标按照 nums[下标] 进行排序
        left = 0
        right = len(nums) - 1

        while left < right:
            sum_re = nums[sorted_id[left]] + nums[sorted_id[right]]
            if sum_re == target:
                return [sorted_id[left], sorted_id[right]]
            elif sum_re > target:
                right -= 1
            else:
                left +=1 

# 思路2
class Solution:
    def twoSum(self, nums, target):
        hash_map = {}
        for index, num in enumerate(nums):
            sub_num = target - num
            if sub_num in hash_map.keys():
                return [hash_map[sub_num], index]
            hash_map[num] = index
        return None



nums = [3,2,4]
target = 6
print(Solution().twoSum(nums, target))
