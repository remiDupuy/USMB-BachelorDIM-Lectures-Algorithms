"""
File containing all tests for S1_algotools
"""

import pytest
import S1_algotools as s

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
