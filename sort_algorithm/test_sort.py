# -*- coding:utf-8 -*-

import pytest

import select_sort
import bubble_sort
import insert_sort
import merge_sort

class TestSort(object):

    def  test_select(self, generate_arr):
 
        # assert sorted(generate_arr) == select_sort.selection_sort_simple(generate_arr)
        assert sorted(generate_arr) == select_sort.selection_sort_high(generate_arr)


    def test_bubble(self, generate_arr):

        # assert sorted(generate_arr) == bubble_sort.bubble_end(generate_arr)
        assert sorted(generate_arr) == bubble_sort.bubble_home(generate_arr)

    def test_insert(self, generate_arr):
        assert sorted(generate_arr) == insert_sort.insert_sort(generate_arr)

    def test_merge(self, generate_arr):
        assert sorted(generate_arr) == merge_sort.merge_simple().merge_sort(generate_arr)