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
            elif nums[0] < nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False