

class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)
        
        def dfs(item, start_index):
            res.append(item)
            for i in range(start_index, n):
                dfs(item+[nums[i]], i+1)

        dfs([], 0)
        return res