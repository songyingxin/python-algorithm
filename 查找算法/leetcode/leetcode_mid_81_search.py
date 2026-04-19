class Solution:
    def search(self, nums: List[int], target: int) -> bool:


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return True
            
            if nums[left] == nums[mid]:
                left += 1
            elif nums[right] == nums[mid]:
                right -= 1
            elif nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left += 1
                else:
                    right -= 1
            else:
                if target >= nums[left] and target < nums[mid]:
                    right -= 1
                else:
                    left += 1

        return False