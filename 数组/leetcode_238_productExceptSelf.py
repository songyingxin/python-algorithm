class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [0 for _ in range(len(nums))]
        if nums.count(0) > 1:
            return result

        multi_val = 1
        for val in nums:
            if val != 0:
                multi_val *= val

        if nums.count(0) == 1:
            result[nums.index(0)] = multi_val
        else:
            for i in range(len(nums)):
                result[i] = multi_val // nums[i]
        return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        for j in range(0, len(nums)-1)[::-1]:
            right[j] = right[j+1] * nums[j+1]
        
        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])
        
        return result
        
# 精简代码
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        res, p, q = [1], 1, 1
        for i in range(len(nums) - 1):  # top triangle
            p *= nums[i]
            res.append(p)
        for i in range(len(nums) - 1, 0, -1):  # bottom triangle
            q *= nums[i]
            res[i - 1] *= q
        return res

