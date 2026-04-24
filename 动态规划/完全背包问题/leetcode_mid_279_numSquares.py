

class Solution:
    def numSquares(self, n: int) -> int:
        n = n+1

        dp = [float('inf') for i in range(n)]
        dp[0] = 0

        for i in range(1, n):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], dp[i-j*j] + 1)
        return dp[-1]

                
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
