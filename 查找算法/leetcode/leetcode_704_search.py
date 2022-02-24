
# 思路1：定义 target 在 [left, right] 区间内
# while (left <= right)， 因为left == right 是有意义的
# if (nums[mid] > target) right 要赋值为 mid - 1，因为当前这个nums[mid]一定不是target，那么接下来要查找的左区间结束下标位置就是 mid - 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  

# 定义 target 在[left, right) 区间内
# while (left < right)，这里使用 < ,因为left == right在区间[left, right)是没有意义的
# if (nums[mid] > target) right 更新为 mid，因为当前nums[mid]不等于target，去左区间继续寻找，而寻找区间是左闭右开区间，所以right更新为mid，即：下一个查询区间不会去比较nums[mid]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left+ right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

