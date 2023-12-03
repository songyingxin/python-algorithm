class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(x, y):
            if grid[x][y] == 0:
                return 0
            
            m = len(grid)
            n = len(grid[0])
            grid[x][y] = 0
            area = 1
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]

                if 0 <= new_x < m and 0 <= new_y < n:
                    area += dfs(new_x, new_y)
            
            return area

        m = len(grid)
        n = len(grid[0])

        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0)
        ]

        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))
        
        return max_area


