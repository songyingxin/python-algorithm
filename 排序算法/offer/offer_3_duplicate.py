# -*- coding:utf-8 -*-

# 思路1: 采用一个 set 维护已经访问过的元素
class Solution:
    def duplicate(self , numbers: List[int]) -> int:
        hash_set = set()
        for val in numbers:
            if val in hash_set:
                return val
            hash_set.add(val)
        
        return -1
            
# 思路2: 数组中元素在 0-n-1 之间，这表明如果数组中没有重复元素，那么数组排序后数字i将出现在下标为i的位置。
# 由于数组中有重复元素，有些位置可能存在多个数字，同时有些位置可能没有数字。
class Solution:
    def duplicate(self , numbers: List[int]) -> int:
        # write code here
        i = 0
        while i < len(numbers):
            if numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    return numbers[i]
                 
                # 注意，此时的交换不能直接采用 numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
                tmp = numbers[i]
                numbers[i], numbers[tmp] = numbers[tmp], numbers[i]
            else:
                i += 1
        return -1

# # 二分思想: 将 1-n 的数字依据中间数组 m 划分， 则划分为两部分：前面一半范围为[1,m]， 后面一半范围为 [m+1, n]。 如果 [1,m] 中的数目超过 m，那么[1,m]这一半内一定包含重复的数字，反之，则重复数字在 [m+1,n]中。

# class Solution:
#     def duplicate(self, numbers):

#         if not numbers:
#             return -1
        
#         start = 0
#         end = len(numbers) - 1

#         while start <= end:

#             middle = (end - start) // 2 + start
#             count = self.count_range(numbers, start, middle)
#             if end == start:
#                 if count > 1:
#                     return start
#                 else:
#                     break
#             if count > middle - start + 1:
#                 end = middle
#             else:
#                 start = middle + 1
            
#         return -1

#     def count_range(self, numbers, start, end):
#         """ 统计 numbers 中处于 [start, end] 之间的个数 """
#         if not numbers:
#             return 0
#         count = 0
#         for i in range(len(numbers)):
#             if numbers[i] >= start and numbers[i] <= end:
#                 count += 1

#         return count
        
# numbers =[2,1,3,1,4]
# print(Solution().duplicate(numbers))