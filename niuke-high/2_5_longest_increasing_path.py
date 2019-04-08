# # 回溯思想， 过不了
# class Solution:
#     def longestIncreasingPath(self, matrix):
#         max_num = 0

#         for row in range(len(matrix)):
#             for col in range(len(matrix[0])):
#                 max_num = max(max_num, self.back_track(matrix, row, col))
        
#         return max_num

#     def back_track(self, matrix, row, col):
        
#         # 左
#         if col > 0 and matrix[row][col-1] > matrix[row][col]:
#             left_path = self.back_track(matrix, row, col-1) + 1
#         else:
#             left_path = 1
        
#         # 上
#         if row > 0 and matrix[row-1][col] > matrix[row][col]:
#             up_path = self.back_track(matrix, row-1, col) + 1
#         else:
#             up_path = 1

#         # 右
#         if col < len(matrix[0]) - 1 and matrix[row][col+1] > matrix[row][col]:
#             right_path = self.back_track(matrix, row, col+1) + 1
#         else:
#             right_path = 1
        
#         # 下
#         if row < len(matrix) - 1 and matrix[row+1][col] > matrix[row][col]:
#             down_path = self.back_track(matrix, row+1, col) + 1
#         else:
#             down_path = 1
        
#         return max(left_path, right_path, up_path, down_path)

# 动态规划
class Solution:
    def longestIncreasingPath(self, matrix):
        max_num = 0
        dp = []
        for i in range(len(matrix)):
            item = [0 for i in range(len(matrix[0]))]
            dp.append(item)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                max_num = max(max_num, self.back_track(matrix, dp, row, col))

        return max_num

    def back_track(self, matrix, dp, row, col):

        if dp[row][col] == 0:

            # 左
            if col > 0 and matrix[row][col-1] > matrix[row][col]:
                left_path = self.back_track(matrix, dp, row, col-1) + 1
            else:
                left_path = 1

            # 上
            if row > 0 and matrix[row-1][col] > matrix[row][col]:
                up_path = self.back_track(matrix, dp, row-1, col) + 1
            else:
                up_path = 1

            # 右
            if col < len(matrix[0]) - 1 and matrix[row][col+1] > matrix[row][col]:
                right_path = self.back_track(matrix, dp, row, col+1) + 1
            else:
                right_path = 1

            # 下
            if row < len(matrix) - 1 and matrix[row+1][col] > matrix[row][col]:
                down_path = self.back_track(matrix, dp, row+1, col) + 1
            else:
                down_path = 1
                
            dp[row][col] = max(left_path, right_path, up_path, down_path)
        return dp[row][col]




nums = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]
print(Solution().longestIncreasingPath(nums))
