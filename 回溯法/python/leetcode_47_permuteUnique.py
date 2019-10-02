class Solution:
    def permuteUnique(self, nums):

        def dfs(nums, item):
            if not nums:
                result.add(tuple(item))
                return

            for i in range(len(nums)):
                tmp = nums[:i] + nums[i+1:]
                tmp_item = item[:]
                tmp_item.append(nums[i])
                dfs(tmp, tmp_item)

        result = set()

        dfs(nums, [])

        return result

if __name__ == "__main__":
    
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))
