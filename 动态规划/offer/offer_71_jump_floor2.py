
# -*- coding:utf-8 -*-

# 思路1： 动态规划方程： f(n) = f(n-1) + ... + f(1), 而 f(n-1) = f(n-2) + ... + f(1) 因此 f(n) = 2f(n-1)
class Solution:
    def jumpFloorII(self , number: int) -> int:
        # write code here
        start_one = 1
        for i in range(1, number):
            start_one = 2 * start_one
        
        return start_one


# 思路2：f(n) = 2f(n-1) = 2^{n-1}
class Solution:
    def jumpFloorII(self , number: int) -> int:
        # write code here
        return 2**(number-1)