
# https://leetcode-cn.com/problems/two-sum/solution/

# 思路1： 暴力枚举
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        return []

# 哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        haxi = {}
        for index, num in enumerate(nums):
            if target - num in haxi:
                return [haxi[target-num], index]
            
            haxi[num] = index
        return []