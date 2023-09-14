# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here

        tmp = []
        for a in array:
            if a in tmp:
                tmp.remove(a)
            else:
                tmp.append(a)
        return tmp

# O(n) 解法
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        res = array[0]
        for val in array[1:]:
            res ^= val

        index = bin(res)[::-1].index('1')
        arr1 = []
        arr2 = []
        for val in array:
            if len(bin(val)) - 2 < index or bin(val)[::-1][index] == '0':
                arr1.append(val)
            else:
                arr2.append(val)

        num1 = arr1[0]
        for val in arr1[1:]:
            num1 ^= val

        num2 = arr2[0]
        for val in arr2[1:]:
            num2 ^= val

        return [num1, num2]

        
if __name__ == "__main__":
    
    arr = [2, 4, 3, 6, 3, 2, 5, 5]

    Solution().FindNumsAppearOnce(arr)
