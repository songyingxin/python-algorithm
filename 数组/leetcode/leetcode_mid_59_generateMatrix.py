class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n-1
        top = 0
        down = n-1

        res = [
            [0] * n for i in range(n)
        ]

        num = 1
        while num <= n*n:
            for i in range(left, right+1):
                res[top][i] = num   
                num += 1
            
            top += 1
            for i in range(top,down+1):
                res[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left-1,-1):
                res[down][i] = num
                num += 1
            down -= 1

            for i in range(down,top-1,-1):
                res[i][left] = num
                num += 1
            left += 1
        return res



