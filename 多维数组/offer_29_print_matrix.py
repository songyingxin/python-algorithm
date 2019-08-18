# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here 

        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        if not matrix or rows == 0 or cols == 0 :
            return result

        left = 0
        top = 0
        right = cols - 1
        bottom = rows - 1

        while left <= right and top <= bottom:
            # [[top, left], [top, right]
            for i in range(left, right+1):
                result.append(matrix[top][i])
            
            # [[top+1, right], [bottom, right]]
            for i in range(top+1, bottom+1):
                result.append(matrix[i][right])

            # [ [bottom, right-1], [bottom, left]]
            if top != bottom:
                for i in range(left, right)[::-1]:
                    result.append(matrix[bottom][i])
            
            # [ [bottom-1, left ], [top+1, left]
            if left != right:
                for i in range(top+1, bottom)[::-1]:
                    result.append(matrix[i][left])
            
            left += 1 
            top += 1
            right -= 1
            bottom -= 1
        
        return result
        

        

        


