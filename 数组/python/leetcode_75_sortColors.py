# 思路1： 计数排序思想
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0, 0, 0]  # 0, 1, 2 出现的次数

        for val in nums:
            count[val] += 1

        #  常规解法
        # for i in range(count[0]):
        #     nums[i] = 0
        # for i in range(count[0], count[0] + count[1]):
        #     nums[i] = 1
        # for i in range(count[0] + count[1], len(nums)):
        #     nums[i] = 2

        # 优化解法，以应对颜色较多时的情况
        k = 0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[k] = i
                k += 1

# 三路排序
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0  # nums[0...zero] = 0
        two = len(nums)-1   # nums[two ... n-1] = 2

        i = 0
        while i <= two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            else:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
                i += 1



# 融入荷兰国旗的解法
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.netherlands_flag(nums, 0, len(nums) - 1, 1)
        print(nums)

    def netherlands_flag(self, arr, low, high, num):
        """ 对数组的一段进行分界
        Args:
            low: 要分界的数组的下界
            high： 要分界的数组的上界
            num: 分界的数
        """

        left = low   # left = 0
        right = high  # right = len(arr) - 1

        current = low  # current = 0

        while current <= right:
            if arr[current] < num:
                arr[left], arr[current] = arr[current], arr[left]
                left += 1
                current += 1
            elif arr[current] > num:
                arr[right], arr[current] = arr[current], arr[right]
                right -= 1
            else:
                current += 1
