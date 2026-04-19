class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def dfs(item, start_index):
            if len(item) > 1:
                res.append(item)

            used = set()
            for i in range(start_index, n):
                # 不是递增直接跳过
                if item and nums[i] < item[-1]:
                    continue

                # 用set去重
                if nums[i] in used:
                    continue
                used.add(nums[i])
                
                dfs(item+[nums[i]], i+1)
        
        dfs([], 0)
        return res