

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


class Solution:
    def subsets(self, nums):

        def dfs(item, index):
            if index == len(nums):
                result.append(item)
                return

            tmp_item = item[:]
            tmp_item.append(nums[index])
            dfs(tmp_item, index+1)

            tmp_item = item[:]
            dfs(tmp_item, index+1)

        result = []
        dfs([], 0)

        return result


