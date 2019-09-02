
# dfs
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row = len(grid)   # 行数
        col = len(grid[0])  # 列数

        result = 0

        def dfs(i,j):
            grid[i][j] = '0'

            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i = i + x
                tmp_j = j + y

                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == '1':
                    dfs(tmp_i, tmp_j)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs[i][j]
                    result += 1

        return result


# bfs

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        result = 0

        def bfs(i,j):
            queue = deque()
            queue.appendleft((i,j))
            grid[i][j] = '0'
            while queue:
                i, j = queue.pop()

                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    tmp_i = i + x
                    tmp_j = j + y

                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == '1':
                        grid[tmp_i][tmp_j] = '0'
                        queue.appendleft((tmp_i, tmp_j))
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    bfs(i,j)
                    result += 1
        
        return result
