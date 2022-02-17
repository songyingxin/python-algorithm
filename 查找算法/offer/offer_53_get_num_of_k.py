

# -*- coding:utf-8 -*-



# 思路1：直接遍历得到 k 的次数
class Solution:
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        # write code here
        times = 0
        for num in data:
            if num == k:
                times += 1
        return times




# 思路2：分别用二分查找找到出现的第一个3的坐标index1和最后一个3的坐标index2， 然后就得到结果： index2 - index1 + 1. 

# - get_first_k: 先找到中间位置 mid。如果 arr[mid] > k ， 则说明 k 只有可能出现在数组的前半段，那么则有 end = mid - 1; 如果 arr[mid] < k， 则说明 k 只有可能出现在数组的后半段， 那么则有 start = mid + 1; 如果 arr[mid] == k, 且arr[mid-1] 也为 k，那么就说明 mid就是第一个出现的 k，考虑到 mid可能为边界 0， 如果mid 为边界0， 那说明 0 就是第一个出现的k， 否则， 则说明第一个 k 在数组的前半段。

# - get_last_k: 先找到中间位置 mid。如果 arr[mid] > k ， 则说明 k 只有可能出现在数组的前半段，那么则有 end = mid - 1; 如果 arr[mid] < k， 则说明 k 只有可能出现在数组的后半段， 那么则有 start = mid + 1; 如果 arr[mid] == k, 且arr[mid+1] 也为 k，那么就说明 mid就是最后一个出现的 k，考虑到 mid可能为边界 len(data)-1， 如果mid 为边界len(data)-1， 那说明 len(data)-1 就是第一个出现的k， 否则， 则说明 最后一个 k 在数组的后半段。

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here

        first_index = self._get_the_first(data, 0, len(data) - 1, k)
        end_index = self._get_the_end(data, 0, len(data) - 1, k)

        if first_index > -1 and end_index > -1:
            return end_index - first_index + 1
        else:
            return 0
    
    def _get_the_first(self, data, start, end, k):

        if start > end:
            return -1

        mid = (start + end) // 2

        if data[mid] == k:
            if (mid > 0 and data[mid - 1] != k) or mid == 0:
                return mid
            else:
                end = mid -1
        elif data[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
        
        return self._get_the_first(data, start, end, k)

    def _get_the_end(self, data, start, end, k):
        if start > end:
            return -1

        mid = (start + end) // 2

        if data[mid] == k:
            if (mid < len(data) - 1 and data[mid+1] != k) or mid == len(data)-1:
                return mid
            else:
                start = mid + 1
        elif data[mid] > k:
            end = mid -1
        else:
            start = mid + 1
        
        return self._get_the_end(data, start, end, k)

            

if __name__ == "__main__":

    # - 测试用例：
    # > - 功能测试： 数组中包含要找的数字； 数组中没有要找的数组； 要查找的数字再数组中出现一次或多次
    # > - 边界测试： 查找数组中的最大值，最小值； 数组中只有一个数字
    # > - 特殊输入： 空数组
    data = [3, 3, 3, 3, 4, 5]

    k = 3

    Solution().GetNumberOfK(data, k)


