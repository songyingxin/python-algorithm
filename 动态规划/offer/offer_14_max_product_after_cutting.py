

# 思路1： 动态规划
# dp[n] = max(dp(i) * dp(n-i))
class Solution:
    def cutRope(self , number: int) -> int:
        # write code here
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        dp = [0 for i in range(number+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, number+1):
            max_len = 0
            for j in range(1, i//2+1):
                product = dp[j] * dp[i-j]
                if max_len < product:
                    max_len = product
                dp[i] = max_len
        return dp[-1]


# 思路2：n>=5 时，尽可能多的剪长度为3的绳子，当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子
class Solution:
    def cutRope(self , number: int) -> int:
        # write code here
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        
        times_3 = number // 3
        if number - times_3 * 3 == 1:
            times_3 -= 1
        
        times_2 = (number - times_3 * 3) // 2
        return 3 ** times_3 * 2 ** times_2