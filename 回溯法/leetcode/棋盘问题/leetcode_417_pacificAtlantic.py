class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        result = []
        rows = len(matrix)
        if rows == 0:
            return result

        cols = len(matrix[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        taiping = [[0] * cols for _ in range(rows)]
        daxi = [[0] * cols for _ in range(rows)]

        def dfs(x, y, flag):

            if visited[x][y] == 1:
                return

            visited[x][y] = 1
            if flag:
                taiping[x][y] = 1
            else:
                daxi[x][y] = 1

            for i, j in directions:
                new_x = x + i
                new_y = y + j

                if not (0 <= new_x < rows and 0 <= new_y < cols):
                    continue

                if matrix[x][y] > matrix[new_x][new_y]:
                    continue

                dfs(new_x, new_y, flag)

        visited = [[0] * cols for _ in range(rows)]
        # 太平洋上方逆流
        for j in range(cols):
            dfs(0, j, True)

        visited = [[0] * cols for _ in range(rows)]
        # 太平洋左边逆流
        for i in range(rows):
            dfs(i, 0, True)

        # 大西洋下方上流
        visited = [[0] * cols for _ in range(rows)]
        for j in range(cols):
            dfs(rows-1, j, False)

        # 大西洋右方左流
        visited = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            dfs(i, cols-1, False)

        for i in range(rows):
            for j in range(cols):
                if taiping[i][j] == 1 and daxi[i][j] == 1:
                    result.append((i, j))

        return result
