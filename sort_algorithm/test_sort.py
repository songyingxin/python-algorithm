# -*- coding:utf-8 -*-

import pytest
import select_sort

class TestSort(object):

    def  test_select(self, generate_arr):
        arr = generate_arr
        assert sorted(arr) == select_sort.selection_sort_simple(arr) 
        assert sorted(arr) == select_sort.selection_sort_high(arr)
