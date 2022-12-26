import pytest

from aoc2022 import day_24 as day


@pytest.fixture
def mock_input():
    return """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""


def test_solve_part1(mock_input):
    expected = 18
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 54
    result = day.solve_part2(mock_input)
    assert expected == result
