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
