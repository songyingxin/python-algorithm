

# https://leetcode-cn.com/problems/matchsticks-to-square/

# DFS
class Solution:
    def makesquare(self, nums: List[int]) -> bool:

        def generate(i, nums, target, bucket):
            if i >= len(nums):
                return bucket[0] == target and bucket[1] == target and bucket[2] == target and bucket[3] == target
            
            for j in range(4):
                if bucket[j] + nums[i] > target:
                    continue
                bucket[j] += nums[i]

                if generate(i+1, nums, target, bucket):
                    return True
                
                bucket[j] -= nums[i]
            
            return False

        if len(nums) < 4:
            return False
        
        square_sum = sum(nums)

        if square_sum % 4 != 0:
            return False
        
        nums.sort(reverse=True)
        bucket = [0] * 4

        return generate(0, nums, square_sum//4, bucket)



        



