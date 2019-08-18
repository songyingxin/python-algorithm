# -*- coding:utf-8 -*-

""" 求取两个数的最大公约数, 注意0与另一个数的最大公约数为这个数 """

""" 1. 穷举法
从 1 到 min(a,b), 看看能不能同时被a, b整除
"""

def GCD1(a, b):
    if a == 0:
        return b

    if b == 0:
        return a

    min_val = min(a,b)

    gcd = 1

    for i in range(2, min_val+1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


""" 2.1 辗转相除法：欧几里算法, 递归版本
gcd(a,b) = gcd(b,a mod b)
"""

def GCD2(a,b):
    if b == 0:
        return a
    return GCD2(b, a % b)

""" 2.2 碾转相除法， 非递归版本 """

def GCD3(a,b):
    while(b!=0):
        c = b
        b = a % b
        a = c
    return a

""" 3. 碾转相减法， 待完善 """

if __name__ == "__main__":
    print(GCD1(0,3))
    print(GCD2(0,3))
    print(GCD3(9,3))
