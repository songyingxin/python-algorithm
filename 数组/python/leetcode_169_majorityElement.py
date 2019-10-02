class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        arr_dict = {}

        for val in nums:
            if val in arr_dict:
                arr_dict[val] += 1
            else:
                arr_dict[val] = 1
            
            if arr_dict[val] > len(nums) // 2:
                return val
    
