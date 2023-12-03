class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        one = 1
        two = 2

        for i in range(3,n+1):
            tmp = one + two
            one = two 
            two = tmp
        
        return two

