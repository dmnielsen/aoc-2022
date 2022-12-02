import pytest

from aoc2022 import day_01 as day


@pytest.fixture
def mock_input():
    return """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_parse_file(mock_input):
    expected = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    result = day.parse_file(mock_input)
    assert all([(cals == result[i][j]) for i, elf in enumerate(expected) for j, cals in enumerate(elf)])


def test_solve_part1(mock_input):
    expected = 24000
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 45000
    result = day.solve_part2(mock_input)
    assert expected == result
