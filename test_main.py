from typing import List

from main import maxArea


def test_maxArea_example_1():
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_maxArea_example_2():
    assert maxArea([1, 1]) == 1
