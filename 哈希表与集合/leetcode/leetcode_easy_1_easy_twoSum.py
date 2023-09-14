
# https://leetcode-cn.com/problems/two-sum/solution/

# 思路：哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        haxi = {}
        for index, num in enumerate(nums):
            if target - num in haxi:
                return [haxi[target-num], index]
            else:
                haxi[num] = index