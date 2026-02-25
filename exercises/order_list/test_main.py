from main import sort_array


def test_sort_array_1():
    assert sort_array([5, 2, 3, 1]) == [1, 2, 3, 5]


def test_sort_array_2():
    assert sort_array([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]


def test_sort_array_3():
    assert sort_array([-1, 2, -8, -10]) == [-10, -8, -1, 2]
