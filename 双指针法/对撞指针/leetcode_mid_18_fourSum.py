class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                now_target = target-nums[i]-nums[j]

                left = j+1
                right = n-1

                while left < right:
                    if left > j+1 and nums[left] == nums[left-1]:
                        left += 1
                        continue
                    
                    now_val = nums[left] + nums[right]
                    if now_val == now_target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                    
                    elif now_val > now_target:
                        right -= 1
                    else:
                        left += 1
        
        return res