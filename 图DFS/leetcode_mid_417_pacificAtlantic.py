class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        res = []
        m = len(matrix)
        n = len(matrix[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        taiping = [[0] * n for _ in range(m)]
        daxi = [[0] * n for _ in range(m)]

        def dfs(x, y, visited):

            if visited[x][y]:
                return

            visited[x][y] = True

            for i, j in directions:
                new_i = x + i
                new_j = y + j

                if new_i <0 or new_i>=m or new_j<0 or new_j>=n:
                    continue

                if matrix[x][y] > matrix[new_i][new_j]:
                    continue

                dfs(new_i, new_j,visited)

        for i in range(m):
            dfs(i,0, taiping)
            dfs(i,n-1,daxi)
        
        for i in range(n):
            dfs(0,i,taiping)
            dfs(m-1,i, daxi)

        for i in range(m):
            for j in range(n):
                if taiping[i][j] and daxi[i][j]:
                    res.append((i, j))

        return res