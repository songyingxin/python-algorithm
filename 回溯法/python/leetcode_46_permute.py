class Solution:
    def permute(self, nums):

        def dfs(vals, item):

            if not vals:
                result.append(item)
                return

            for i in range(len(vals)):
                tmp = vals[:i] + vals[i+1:]
                tmp_item = item[:]
                tmp_item.append(vals[i])
                dfs(tmp, tmp_item)

        result = []
        dfs(nums, [])

        return result


if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))
