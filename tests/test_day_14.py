import pytest

from aoc2022 import day_14 as day


@pytest.fixture
def mock_input():
    return """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def test_solve_part1(mock_input):
    expected = 24
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 93
    result = day.solve_part2(mock_input)
    assert expected == result
