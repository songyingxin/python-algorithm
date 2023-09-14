
# https://leetcode-cn.com/problems/search-insert-position


# 思路2： 二分查找，本质上是查找位置 nums[pos-1] < target <= nums[pos]
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        res = len(nums)

        left = 0
        right = len(nums) -1
        
        while left <= right:
            mid = (left+right) // 2
            if target <= nums[mid]:
                res = mid
                right = mid-1
            else:
                left = mid + 1
        return res



