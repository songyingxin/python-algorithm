# -*- coding:utf-8 -*-


class Solution_simple:
    """ 思路1 , 暴力解法 """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]


class Solution_middle:
    """ 思路2 , 二分查找 """

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            left, right = i+1, len(numbers)-1
            real_target = target - numbers[i]

            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == real_target:
                    return [i+1, mid+1]
                elif numbers[mid] > real_target:
                    right = mid -1
                else:
                    left = mid + 1


class Solution_high:
    """ 思路3 , 对撞指针"""

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1


class Solution_high:
    """ 思路4 , 采用字典来做"""

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9

    print(Solution_middle().twoSum(numbers, target))

