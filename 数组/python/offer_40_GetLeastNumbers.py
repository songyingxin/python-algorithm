import heapq


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k <= 0 or k > len(tinput):
            return []
        return heapq.nsmallest(k, tinput)


# 解法1: 时间复杂度为 O(n)
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k <= 0 or k > len(tinput):
            return []
        start = 0
        end = len(tinput) - 1
        index = self.partition(tinput, start, end)

        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.partition(tinput, start, end)
            else:
                start = index + 1
                index = self.partition(tinput, start, end)
        result = sorted(tinput[:k])
        return result

    def partition(self, arr, low, high):
        left = low
        right = high

        current = low
        num = arr[high]
        while current <= right:
            # 如果当前元素小于partition 元素，则arr[left] 与 arr[current] 交换， left++
            if arr[current] < num:
                arr[left], arr[current] = arr[current], arr[left]
                left += 1
                current += 1
            # 如果当前元素大于partition 元素，则arr[left] 与 arr[current] 交换， right++
            elif arr[current] > num:
                arr[right], arr[current] = arr[current], arr[right]
                right -= 1
            # 如果相等，则不变
            else:
                current += 1

        return left
