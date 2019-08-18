#! /usr/bin/env python
# -*- coding: utf-8 -*-

def palindrome_number_simple(number):
    """ 对于思路 2 的实现
    Args：
        number： 回文数
    Returns
        True: 是否为回文数
        False:
    """
    if(number) < 0:
        return False

    help = 1

    while (number/help) >= 10:
        help *= 10

    while number != 0:
        if number/help != number % 10: # 最高位与最低位比较
            return False

        number = (number % help) / 10  # 裁剪掉最高位与最低位
        help /= 100

    return True


def palindrome_number_str(number):
    """ 对于思路1 的实现 """
    num_str = str(number)
    times = int(len(num_str) / 2)

    for i in range(times):
        begin = num_str[i]
        end = num_str[-i-1]
        if begin != end:
            return False

    return True


if __name__ == "__main__":

    # assert palindrome_number_simple(123321) == True
    # assert palindrome_number_simple(12321) == True
    # assert palindrome_number_simple(12345) == False

    assert palindrome_number_str(123321) == True
    assert palindrome_number_str(12321) == True
    assert palindrome_number_str(12345) == False
