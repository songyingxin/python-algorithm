# -*- coding:utf-8 -*-

import random

def get_random_array(max_size, min_value, max_value):
    return [random.randint(min_value, max_value) for i in range(max_size)]


