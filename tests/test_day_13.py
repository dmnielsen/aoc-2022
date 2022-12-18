import pytest

from aoc2022 import day_13 as day


@pytest.fixture
def mock_input():
    return """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


@pytest.mark.parametrize(
    'left, right, expected',
    [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], True),
        ([[1], [2, 3, 4]], [[1], 4], True),
        ([9], [[8, 7, 6]], False),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4], True),
        ([7, 7, 7, 7], [7, 7, 7], False),
        ([], [3], True),
        ([[[]]], [[]], False),
        ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9], False),
    ],
)
def test_is_right_order(left, right, expected):
    result = day.is_right_order(left, right)
    assert expected == result


def test_solve_part1(mock_input):
    expected = 13
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 140
    result = day.solve_part2(mock_input)
    assert expected == result
