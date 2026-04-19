class Solution:
    def combinationSum(self, candidates, target):
        res = []
        n = len(candidates)

        def dfs(item, start_index, sum_val):
            if sum_val == target:
                res.append(item)
                return

            if sum_val > target:
                return

            for i in range(start_index, len(candidates)):
                dfs(item + [candidates[i]], i, sum_val + candidates[i])

        dfs([], 0, 0)
        return res
