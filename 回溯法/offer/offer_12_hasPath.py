class Solution:

    def hasPath(self, board, word):

        def search_word(index, x, y):
            if index == len(word) - 1:
                return board[x][y] == word[index]

            if board[x][y] == word[index]:
                masked[x][y] = True
                for direction in directions:
                    new_x = x + direction[0]
                    new_y = y + direction[1]

                    if 0 <= new_x < rows and 0 <= new_y < cols and not masked[new_x][new_y] and search_word(index+1, new_x, new_y):
                        return True
                masked[x][y] = False
            return False

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        rows = len(board)
        if rows == 0:
            return False

        cols = len(board[0])

        masked = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if search_word(0, i, j):
                    return True

        return False