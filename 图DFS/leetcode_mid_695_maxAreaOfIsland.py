class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        directiones = [(0,1), (0,-1), (1,0), (-1,0)]

        res = 0
        def dfs(i,j):

            if grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0
            area = 1
            
            for direction in directiones:
                new_i = i + direction[0]
                new_j = j + direction[1]

                if new_i <0 or new_i>=m or new_j<0 or new_j>=n:
                    continue
                area += dfs(new_i, new_j)
            
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
        
        return res