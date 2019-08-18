class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        start_1 = 1
        start_2 = 2

        for i in range(3, n+1):
            start_1, start_2 = start_2, start_1 + start_2
        
        return start_2

