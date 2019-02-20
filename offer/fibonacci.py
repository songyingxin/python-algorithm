# -*- coding:utf-8 -*-
# class Solution:
#     def Fibonacci(self, n):
#         # write code here

#         if n <= 0:
#             return 0
        
#         if n == 1:
#             return 1
        
#         return self.Fibonacci(n-1) + self.Fibonacci(n-2)


class Solution:
    def Fibonacci(self, n):
        # write code here

        start_one = 0
        start_two = 1

        for i in range(n):

            start_one, start_two = start_two, start_one + start_two

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


class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        
        return 2**(number-1)



if __name__ == "__main__":

    print(Solution().Fibonacci(3))  

