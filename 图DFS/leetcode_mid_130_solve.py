class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directiones = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(i,j):
            
            if board[i][j] != 'O':
                return 
            
            board[i][j] = 'B'
            for direction in directiones:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if new_i <0 or new_i>=m or new_j<0 or new_j>=n:
                    continue
                dfs(new_i,new_j)
        

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


