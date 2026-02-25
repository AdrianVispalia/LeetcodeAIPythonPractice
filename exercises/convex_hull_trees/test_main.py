from main import outerTrees


def test_outerTrees_example_1():
    points = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
    # Expected output can be in any order.
    # One possible output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
    # We will use sorted tuples for comparison.
    expected = [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]

    result = outerTrees(points)

    # Check if result is not None (since implementation is just pass)
    if result is None:
        assert False, "Function returned None"

    assert sorted([tuple(x) for x in result]) == sorted([tuple(x) for x in expected])


def test_outerTrees_example_2():
    points = [[1, 2], [2, 2], [4, 2]]
    expected = [[4, 2], [2, 2], [1, 2]]

    result = outerTrees(points)

    if result is None:
        assert False, "Function returned None"

    assert sorted([tuple(x) for x in result]) == sorted([tuple(x) for x in expected])
