
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
    def subsetsWithDup(self, nums):

        def dfs(item, index):
            if index == len(nums):
                item.sort()
                result.add(tuple(item))
                return

            tmp_item = item[:]
            tmp_item.append(nums[index])
            dfs(tmp_item, index+1)

            tmp_item = item[:]
            dfs(tmp_item, index+1)

        result = set()
        dfs([], 0)
        return result
