class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x, y):
            grid[x][y] = '0'

            for direction in directions:
                new_x, new_y = x+direction[0], y+direction[1]

                if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == '1':
                    dfs(new_x, new_y)

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        rows = len(grid)
        if rows == 0:
            return 0

        cols = len(grid[0])
        result = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    result += 1
                    dfs(i, j)

        return result
