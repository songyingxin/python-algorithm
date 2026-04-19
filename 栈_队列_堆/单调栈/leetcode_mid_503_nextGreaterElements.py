class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack = []
        res = [-1] * len(nums)

        for i in range(2*len(nums)):
            i = i % len(nums)
            val = nums[i]
            while stack and val > nums[stack[-1]]:
                pre_index = stack.pop()
                res[pre_index] = val
            
            stack.append(i)
        
        return res