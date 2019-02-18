# -*- coding:utf-8 -*-

"""
duplication[0]: 存储重复的数字
返回值： 有重复数字：True， 无重复数字：False
"""

class Solution_hash:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        """ 实现方法类似散列表，但比散列表所占用空间更小 """
        flag = False
        c = collections.Counter(numbers)
        for k, v in c.items():
            if v > 1:
                duplication[0] = k
                flag = True
                break
        return flag


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        """ 最佳方法 """
        i = 0
        is_flag = False
        while i < len(numbers):

            if numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    is_flag = True
                    break
                tmp = numbers[i]
                numbers[i], numbers[tmp] = numbers[tmp], numbers[i]
            else:   
                i += 1
        return is_flag




if __name__ == "__main__":
    
    num = [2,3,1,0,2,5,3]
    dup = [1]
    Solution().duplicate(num,dup)
    print(dup)


