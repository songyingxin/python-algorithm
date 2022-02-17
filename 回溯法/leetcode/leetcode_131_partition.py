class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(s, item):
            if not s:
                res.append(item)

            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], tmp + [s[:i]])

        dfs(s,[])
        return res


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
        #print(dp)
        res = []

        def dfs(i, tmp):
            if i == n:
                res.append(tmp)
            for j in range(i, n):
                if dp[i][j]:
                    dfs(j + 1, tmp + [s[i: j + 1]])

        dfs(0, [])
        return res