
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        n = len(nums)

        def dfs(item, start_index):
            res.append(item)

            for i in range(start_index, n):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                dfs(item+[nums[i]], i+1)
        
        dfs([], 0)
        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        n = len(nums)

        def dfs(item, start_index):
            res.append(item)

            used = set()
            for i in range(start_index, n):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                dfs(item+[nums[i]], i+1)
        
        dfs([], 0)
        return res