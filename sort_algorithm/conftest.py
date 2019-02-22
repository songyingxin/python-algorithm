# -*- coding:utf-8 -*-
import random
import pytest

@pytest.fixture
def  generate_arr():
    """ 生成 num个数字，left < 元素 < right 
    Args:
        num: 元素个数
        left: 元素的左边界
        right： 元素的右边界

    Returns:
        arr: 生成的无序数组
    """
    return [random.randint(1, 10) for i in range(100)]

arr = generate_arr()
print(arr)