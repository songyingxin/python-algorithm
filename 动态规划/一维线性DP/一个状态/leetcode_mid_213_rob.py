class Solution:
    def rob(self, nums: List[int]) -> int:


        def sub_rob(sub_nums):
            one = sub_nums[0]
            two = max(sub_nums[:2])

            for num in sub_nums[2:]:
                one, two = two, max(one+num, two)
            
            return two
        
        n = len(nums)
        if n < 3:
            return max(nums)
        else:
            left = sub_rob(nums[:-1])
            right = sub_rob(nums[1:])
            
            return max(left, right)