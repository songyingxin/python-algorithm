class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        def dfs(item, start_index):
            if start_index == len(nums):
                for val in item:
                    if val != self.nums_avg:
                        return False
                return True
            
            for i in range(k):
                if item[i] + nums[start_index] > self.nums_avg:
                    continue
                
                if i > 0 and item[i] == item[i-1]:
                    continue

                item[i] += nums[start_index]
                if dfs(item, start_index+1):
                    return True
                item[i] -= nums[start_index]
            return False
        
        if len(nums) < k:
            return False
        
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False

        self.nums_avg = nums_sum // k 
        for val in nums:
            if val > self.nums_avg:
                return False

        nums.sort(reverse=True)
        item = [0] * k  
        return dfs(item, 0)
        