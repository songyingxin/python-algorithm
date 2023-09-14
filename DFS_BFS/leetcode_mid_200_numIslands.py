class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        res = 0

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 
            
            if grid[i][j] == '0':
                return

            grid[i][j] = '0'

            for direction in directions:
                new_x = i + direction[0]
                new_y = j + direction[1]
                dfs(new_x, new_y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        
        return res