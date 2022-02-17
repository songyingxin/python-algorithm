

# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# 思路1：顺序查找

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        begin = -1
        end = -1

        for index, num in enumerate(nums):
            if num == target and begin == -1:
                begin = index
            
            if num > target:
                end = index - 1
                break
            if begin != -1 and index == len(nums) -1:
                end = len(nums)-1
                break
        
        return [begin,end]

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






def find_left(nums, target):
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

def find_right(nums, target):
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

nums = [5,7,7,8,8,8,8,10]
target = 9

print(find_left(nums, target))
print(find_right(nums, target))
