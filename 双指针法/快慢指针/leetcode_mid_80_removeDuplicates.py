
# 常规解法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 1
        pre = nums[0]  # 前一个出现的数
        times = 1  # 出现次数
        for i in range(1, len(nums)):
            if nums[i] != pre:
                nums[left] = nums[i]
                left += 1
                pre = nums[i]
                times = 1
            else:
                if times == 1:
                    nums[left] = nums[i]
                    left += 1
                    times += 1

        return left


# 牛逼解法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1

        return i

