class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        row = len(dungeon)
        col = len(dungeon[0])

        dp = [[0] * col for _ in range(row)]

        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)
        
        for i in range(col -2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i+1] - dungeon[-1][i])
        
        for i in range(row-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1] - dungeon[i][-1])
        
        for i in range(row-2, -1, -1):
            for j in range(col-2, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        
        return dp[0][0]




