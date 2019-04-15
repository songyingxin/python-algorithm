class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        help_arr = [nums[i] + i for i in range(len(nums))]  # 可优化
        current = 0  # 当前位置
        max_jump = help_arr[0]
        result = 1
        while max_jump < len(nums) - 1:
            tmp_arr = help_arr[current: max_jump+1]   # 可优化
            max_jump = max(tmp_arr)
            current = current + tmp_arr.index(max_jump)
            result += 1
        return result

# 优化版本


class Solution:
    def jump(self, nums):
        if not nums:
            return 0
        result = 0
        current = 0
        next_step = 0
        for i in range(len(nums)):
            if current < i:
                result += 1
                current = next_step
            next_step = max(next_step, i + nums[i])
        return result


nums = [2, 3, 1, 1, 4]
print(Solution().jump(nums))


