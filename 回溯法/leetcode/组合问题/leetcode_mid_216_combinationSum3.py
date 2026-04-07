class Solution:
    def combinationSum3(self, k, n):
        res = []

        def dfs(item, start_index, sum_val):
            if len(item) == k:
                if sum_val == n:
                    res.append(item)
                return
            
            for i in range(start_index, 10):
                dfs(item+[i], i+1, sum_val+i)
        
        dfs([], 1, 0)

        return res
            