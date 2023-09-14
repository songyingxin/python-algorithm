class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        # 先旋转行
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1
        
        # 再旋转列
        for j in range(1, n):
            num_0 = 0
            for i in range(m):
                if grid[i][j] == 0:
                    num_0 += 1
            if num_0 > m // 2:
                for i in range(m):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1
        
        # 计算最终值
        res = 0
        for i in range(m):
            now_val = 0
            for j in range(n):
                now_val = now_val * 2 + grid[i][j]
            
            res += now_val
        
        return res


if __name__ == "__main__":
    
    A = [[0, 1], [1, 1]]
    print(Solution().matrixScore(A))
