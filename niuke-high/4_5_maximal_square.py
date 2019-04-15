class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        max_val = 0
        result = []
        for i in range(len(matrix)):
            result.append([0 for i in range(len(matrix[0]))])
        
        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                result[i][0] = 1
                max_val = 1
            else:
                result[i][0] = 0
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                result[0][i] = 1
                max_val = 1
            else:
                result[0][i] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    result[i][j] = min(result[i-1][j-1], result[i-1][j], result[i][j-1]) + 1
                    max_val = max(max_val, result[i][j])
                else:
                    result[i][j] = 0
        
        return max_val ** 2
                

matrix = [
    ["0", "0", "0", "1"], 
    ["1", "1", "0", "1"], 
    ["1", "1", "1", "1"], 
    ["0", "1", "1", "1"], 
    ["0", "1", "1", "1"]]

print(Solution().maximalSquare(matrix))
