


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        pre = 1
        pre_pre = 0
        for i in range(2, n+1):
            pre, pre_pre = pre_pre+pre, pre
        
        return pre