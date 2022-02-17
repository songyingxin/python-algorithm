

# permute(nums[0...n-1]) = (取出一个数字) + permute(nums[0...n-1] - 这个数字)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        def backtracking(nums, item):
            if not nums:
                result.append(item)
                return
            
            for index in range(len(nums)):
                tmp = nums[:index] + nums[index+1:]
                tmp_item = item[:]
                tmp_item.append(nums[index])
                backtracking(tmp, tmp_item)

        result = []
        backtracking(nums, [])
        return result


if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))
