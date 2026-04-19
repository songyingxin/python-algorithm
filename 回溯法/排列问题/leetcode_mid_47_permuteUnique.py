

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n 
        nums.sort()

        def dfs(item):
            if len(item) == n:
                res.append(item)
                return
            
            for i in range(n):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                dfs(item+[nums[i]])
                used[i] = False
        
        dfs([])
        return res






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
