"""
File containing all tests for S1_algotools
"""

import pytest
import S1_algotools as s
import numpy

## Functions to test average_above_zero function
def test_average_above_zero_4():
    input_list = [3, 5, -1, 0]
    assert s.average_above_zero(input_list) == 4


def test_average_above_zero_allNegatives():
    input_list = [-2, -5, -1, -3]
    assert s.average_above_zero(input_list) == 0


def test_average_above_zero_0():
    input_list = [0, 0, 0]
    assert s.average_above_zero(input_list) == 0

def test_average_above_zero_empty():
    input_list = []
    assert s.average_above_zero(input_list) == 0

## End test average_above_zero


## Functions to test max_value function
def test_max_value_5():
    input_list = [3, 5, -1, 0]
    assert s.max_value(input_list) == 5

def test_max_value_negative2():
    input_list = [-2, -4, -10, -34]
    assert s.max_value(input_list) == -2

def test_max_value_0():
    input_list = [-4, -5, -1, 0]
    assert s.max_value(input_list) == 0


def test_max_value_empty():
    input_list = []
    with pytest.raises(ValueError):
        s.max_value(input_list)
# End test max_value


## Tests reserve_table
def test_reverse_table_4321():
    input_list = [1,2,3,4]
    assert s.reverse_table(input_list) == [4,3,2,1]


def test_reverse_table_empty():
    input_list = []
    with pytest.raises(ValueError):
        s.reverse_table(input_list)


def test_reverse_table_moins1000_moins3_0_5():
    input_list = [5,0,-3,-1000]
    assert s.reverse_table(input_list) == [-1000, -3, 0, 5]
##END reserve table


## Tests for Roi Bbox
def test_roi_bbox_1():
    size_rows = 10
    size_cols = 10
    mtx = numpy.zeros([size_rows, size_cols])
    mtx[4:7, 7:9] = numpy.ones([3, 2])
    mtx[2:4, 5:8] = numpy.ones([2, 3])
    assert s.roi_bbox(mtx) == ((2, 6), (5, 8))

def test_roi_bbox_0():
    size_rows = 10
    size_cols = 10
    mtx = numpy.zeros([size_rows, size_cols])
    with pytest.raises(ValueError):
        s.roi_bbox(mtx)


def test_roi_bbox_full_ones():
    size_rows = 10
    size_cols = 10
    mtx = numpy.ones([size_rows, size_cols])
    assert s.roi_bbox(mtx) == ((0, 9), (0, 9))
#End roi bbox


## Tests for random_fill_parse
def test_random_fill_parse():
    size_rows = 5
    size_cols = 5
    mtx = numpy.zeros([size_rows, size_cols], dtype=str)
    with pytest.raises(ValueError):
        s.random_fill_sparse(mtx, 26)
#End random_fill_parse