# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        ugly_list = [1]
        index_2 = 0
        index_3 = 0
        index_5 = 0

        for i in range(index-1):
            new_ugly = min(ugly_list[index_2] * 2, ugly_list[index_3] * 3, ugly_list[index_5] * 5)
            ugly_list.append(new_ugly)

            if new_ugly == 2 * ugly_list[index_2]:
                index_2 += 1
            
            if new_ugly ==  3 * ugly_list[index_3]:
                index_3 += 1
            
            if new_ugly  == 5 * ugly_list[index_5]:
                index_5 += 1

        return ugly_list[-1]


if __name__ == "__main__":
    print(Solution().GetUglyNumber_Solution(10))