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
