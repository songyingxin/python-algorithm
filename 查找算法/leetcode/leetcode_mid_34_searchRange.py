

# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# 思路2：二分查找。 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_left(nums, target)
        right = self.find_right(nums, target)
        return [left, right]

    def find_left(self, nums, target):
        left = 0
        right = len(nums) -1
        is_searched = False
        
        while left <= right:
            mid = (left+right) // 2
            if target == nums[mid]:
                right = mid-1
                is_searched = True
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid + 1
        res = left if is_searched else -1
        return res

    def find_right(self, nums, target):
        left = 0
        right = len(nums) -1
        is_searched = False
        
        while left <= right:
            mid = (left+right) // 2
            if target == nums[mid]:
                is_searched = True
                left = mid + 1
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid + 1

        res = right if is_searched else -1
        return res