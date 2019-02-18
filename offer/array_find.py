# -*- coding:utf-8 -*-


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        row = 0  # 行数
        column = len(array[0]) - 1  # 列数

        while row < len(array) and column >= 0:
            if array[row][column] == target:
                return True
            elif array[row][column] < target:
                row += 1
            else:
                column -= 1
        
        return False


if __name__ == "__main__":
    arr = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    tar = 7

    print(Solution().Find(tar, []))
