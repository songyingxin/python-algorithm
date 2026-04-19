class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        one = 1
        two = 2
        
        for i in range(3, n+1):
            one, two = two, one + two
        
        return two


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp = [1] * (n+1)
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]