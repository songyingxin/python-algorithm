class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        start = 0  # 起始位置横, 纵坐标

        end = len(matrix) -1  # 终止位置横，纵坐标

        while start < end:
            self.rotate_matrix(matrix, start, end)
            start += 1
            end -= 1
    
    def rotate_matrix(self, matrix, start, end):
        for i in range(end - start):
            tmp = matrix[start][start+i]
            matrix[start][start+i] = matrix[end-i][start]
            matrix[end-i][start] = matrix[end][end-i]
            matrix[end][end-i] = matrix[start+i][end] 
            matrix[start+i][end] = tmp
  
        
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(Solution().rotate(matrix))