# dfs
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            board[x][y] = "B"
            for direc_x, direc_y in directions:
                new_x = x + direc_x
                new_y = y + direc_y
                if 1 <= new_x < row and 1 <= new_y < col and board[new_x][new_y] == "O":
                    dfs(new_x, new_y)

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                dfs(row - 1, j)

        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][col-1] == "O":
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"
