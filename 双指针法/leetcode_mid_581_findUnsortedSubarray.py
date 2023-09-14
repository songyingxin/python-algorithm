class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n  = len(nums)

        min_val = nums[n-1]
        left = -1

        max_val = nums[0]
        right = -1

        for i in range(n):
            if nums[i] < max_val:
                right = i 
            else:
                max_val = nums[i]
            
            if nums[n-i-1] > min_val:
                left = n - i - 1
            else:
                min_val = nums[n-i-1]
            
        
        return 0 if left == -1 else right - left + 1