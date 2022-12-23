import pytest

from aoc2022 import day_23 as day


@pytest.fixture
def mock_input():
    return """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""


def test_solve_part1(mock_input):
    expected = 110
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 20
    result = day.solve_part2(mock_input)
    assert expected == result
