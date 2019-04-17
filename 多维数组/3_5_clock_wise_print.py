# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        start_row = 0  # 起始位置横坐标
        start_col  = 0  # 起始位置纵坐标

        end_row = len(matrix) - 1   # 起始位置横坐标
        end_col  = len(matrix[0]) -1 # 起始位置纵坐标

        while start_row <= end_row and start_col <= end_col:
            result.extend(self.print_edge(matrix, start_row, start_col, end_row, end_col))
            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1
        return result

    def print_edge(self, matrix, start_row, start_col, end_row, end_col):
        result = []
        # 当只剩下一行时， 直接添加这行即可结束
        if start_row == end_row:
            # (start_row, start_col) --> (start_row, end_col)
            result.extend(matrix[start_row][start_col:end_col+1])
        # 当只剩下一列的时候， 直接添加这列
        elif start_col == end_col:
            # (start_row, start_col) --> (end_row, start_col)
            for i in range(start_row, end_row+1):
                result.append(matrix[i][start_col])
        else:
            # (start_row, start_col) -->  (start_row, end_col-1)
            result.extend(matrix[start_row][start_col:end_col])

            # (start_row, end_col) --> (end_row-1, end_col)
            for i in range(start_row, end_row):
                 result.append(matrix[i][end_col])

            # (end_row, end_col) -- > (end_row, start_col + 1)
            result.extend(matrix[end_row][start_col +1 : end_col + 1][::-1])

            # (end_row, start_col) --> (start_row+1, start_col)
            for i in range(start_row+1, end_row+1)[::-1]:
                 result.append(matrix[i][start_col])
        return result
                






# nums = [[1]]
# nums = [[1], [2], [3], [4], [5]]
nums = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nums = [[1], [2], [3], [4], [5]]
print(Solution().printMatrix(nums))
            


    
    
