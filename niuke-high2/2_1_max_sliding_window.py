class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k > len(nums):
            return []

        result = []
        help_arr = []
        left = 0
        right = 0

        for i in range(k):
            right  =  i
            while help_arr and nums[help_arr[-1]] <=  nums[right]:
                help_arr.pop()
            help_arr.append(right)
        result.append(nums[help_arr[0]])

        left += 1
        right += 1

        while right < len(nums):

            # right 向右移动一格
            while help_arr and nums[help_arr[-1]] <= nums[right]:
                help_arr.pop()
            help_arr.append(right)

            # left 向左移动一格
            if left > help_arr[0]:
                help_arr.pop(0)
            
            result.append(nums[help_arr[0]])
            right += 1
            left += 1
        
        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 10

print(Solution().maxSlidingWindow(nums, k))


