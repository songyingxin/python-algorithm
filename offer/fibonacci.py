# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here

        if n <= 0:
            return 0
        
        if n == 1:
            return 1
        
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)


class Solution:
    def Fibonacci(self, n):
        # write code here

        start_one = 0
        start_two = 1

        for i in range(n):
             
             tmp = start_one
             start_one = start_two
             start_two = tmp + start_two

        return start_one

""" 青蛙跳台阶 """
class Solution:
    def jumpFloor(self, number):
        # write code here

        start_one = 1
        start_two = 1

        for i in range(number):

            start_one, start_two = start_two, start_one + start_two

        return start_one

# 变态跳台阶
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        
        return 2**(number-1)


#  矩形覆盖
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0

        one = 1
        two = 2
        for i in range(number-1):
            tmp = one
            one = two
            two = tmp + two
        return one


if __name__ == "__main__":

    print(Solution().Fibonacci(3))  

