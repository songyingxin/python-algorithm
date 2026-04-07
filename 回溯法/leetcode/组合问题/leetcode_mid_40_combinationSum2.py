class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(item, start_index, sum_val):
            if sum_val == target:
                res.append(item)
                return

            if sum_val > target:
                return

            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                dfs(item+[candidates[i]], i+1, sum_val + candidates[i])

        
        dfs([], 0, 0)
        return res
