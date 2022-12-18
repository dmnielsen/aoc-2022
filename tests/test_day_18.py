import pytest

from aoc2022 import day_18 as day


@pytest.fixture
def mock_input():
    return """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""


def test_are_connected():
    cube1 = day.Cube(1, 1, 1)
    cube2 = day.Cube(2, 1, 1)
    expected = 1
    result = day.are_connected(cube1, cube2)
    assert expected == result


def test_solve_part1(mock_input):
    expected = 64
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 58
    result = day.solve_part2(mock_input)
    assert expected == result
