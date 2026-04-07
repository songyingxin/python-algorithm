


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        zero = 0
        one = 1

        for i in range(2, n+1):
            zero, one = one, zero+one
        
        return one