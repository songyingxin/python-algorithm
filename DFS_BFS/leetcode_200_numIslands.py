

# https://leetcode-cn.com/problems/number-of-islands/

# DFS，深度优先遍历，将每一个扫描过的标记为0

from re import A


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def DFS(grid, row, col, rows, cols):
            grid[row][col] = '0'

            if row > 0 and grid[row-1][col] == '1':
                DFS(grid, row-1, col, rows, cols)
            
            if row < rows - 1 and grid[row+1][col] == '1':
                DFS(grid, row+1, col, rows, cols)
            
            if col > 0 and grid[row][col-1] == '1':
                DFS(grid, row, col - 1, rows, cols)
            
            if col < cols-1 and grid[row][col+1] == '1':
                DFS(grid, row, col+1, rows, cols)
        
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    result += 1
                    DFS(grid, i, j, rows, cols)
        
        return result

# BFS，广度优先遍历
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        result = 0

        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == '1'):
                    result += 1
                    grid[i][j] = '0'
                    queue = [(i,j)]
                    while queue:
                        row, col = queue.pop(0)
                        if row > 0 and grid[row-1][col] == '1':
                            queue.append((row-1, col))
                            grid[row-1][col] = '0'
                        
                        if row < rows-1 and grid[row+1][col] == '1':
                            queue.append((row+1, col))
                            grid[row+1][col] = '0'
                        
                        if col > 0 and grid[row][col-1] == '1':
                            queue.append((row, col-1))
                            grid[row][col-1] = '0'
                        
                        if col < cols-1 and grid[row][col+1] == '1':
                            queue.append((row, col+1))
                            grid[row][col+1] = '0'
        
        return result




        