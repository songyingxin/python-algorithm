
# dp
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            j = 1
            while i-j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]

                
# 四平方定理
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0: 
            n /= 4 
        if n % 8 == 7: 
            return 4 
        a = 0 
        while a**2 <= n: 
            b = int((n - a**2)**0.5) 
            if a**2 + b**2 == n: 
                return (not not a) + (not not b) 
            a += 1 
        return 3
