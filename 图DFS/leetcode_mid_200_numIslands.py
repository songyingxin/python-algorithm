class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0
        directiones = [(0,1), (0,-1), (1,0), (-1,0)]
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            
            if grid[i][j] == '0':
                return
            
            grid[i][j] = '0'

            for direction in directiones:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if new_i <0 or new_i>=m or new_j<0 or new_j>=n:
                    continue
                dfs(new_i, new_j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i,j)
        
        return res


        