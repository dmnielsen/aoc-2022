import pytest

from aoc2022 import day_22 as day


@pytest.fixture
def mock_input():
    return """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""


def test_solve_part1(mock_input):
    expected = 6032
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 5031
    result = day.solve_part2(mock_input, True)
    assert expected == result
