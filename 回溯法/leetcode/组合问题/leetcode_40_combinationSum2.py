class Solution:
    def combinationSum2(self, candidates, target):

        def dfs(item, sum_val, index):
            if sum_val == target:
                result.append(item)
                return
            if index > len(candidates):
                return

            if sum_val > target:
                return

            for i in range(index, len(candidates)):
                tmp_item = item[:]
                tmp_item.append(candidates[i])
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                dfs(tmp_item, sum_val + candidates[i], i+1)

        result = []
        candidates.sort()
        dfs([], 0, 0)
        return result
