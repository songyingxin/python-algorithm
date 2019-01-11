# -*- coding:utf-8 -*-

import pytest
import select_sort
import bubble_sort

class TestSort(object):

    def  test_select(self, generate_arr):
        arr = generate_arr
        assert sorted(arr) == select_sort.selection_sort_simple(arr) 
        assert sorted(arr) == select_sort.selection_sort_high(arr)


    def test_bubble(self, generate_arr):
        arr = generate_arr

        assert sorted(arr) == bubble_sort.bubble_sort(arr)