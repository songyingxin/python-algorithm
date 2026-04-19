
# https://leetcode-cn.com/problems/two-sum/solution/

# 思路：哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already = {}
        for i, num in enumerate(nums):
            sub_val = target - num 
            if sub_val in already:
                return [already[sub_val], i]
            already[num] = i