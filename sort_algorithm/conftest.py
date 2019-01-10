# -*- coding:utf-8 -*-
import random
import pytest

@pytest.fixture(scope="class")
def  generate_arr():
    """ 生成 num个数字，left < 元素 < right 
    Args:
        num: 元素个数
        left: 元素的左边界
        right： 元素的右边界

    Returns:
        arr: 生成的无序数组
    """
    return [random.randint(1, 10000) for i in range(1000)]

print(type(generate_arr))