import pytest

from aoc2022 import day_12 as day


@pytest.fixture
def mock_input():
    return """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def test_solve_part1(mock_input):
    expected = 31
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 29
    result = day.solve_part2(mock_input, test=True)
    assert expected == result
