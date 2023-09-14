

# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

# 二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0 
        right = len(nums) - 1 

        res = -1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                res = mid
            
            # 左边子数组有序,
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # 右边子数组有序
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    left = mid + 1
                else:
                    right = mid -1
        return res
                

                




