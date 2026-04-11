class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        used = [
            [False] * n for _ in range(m)
        ]

        directiones = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def dfs(i,j,word_index):
        
            # 是否已用
            if used[i][j]:
                return False
            
            if board[i][j] != word[word_index]:
                return False   
            
            if word_index == len(word)-1:
                return True
            
            used[i][j] = True
            for direction in directiones:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if new_i <0 or new_i>=m or new_j<0 or new_j>=n:
                    continue
                if dfs(new_i, new_j, word_index+1):
                    return True
            used[i][j] = False
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False



