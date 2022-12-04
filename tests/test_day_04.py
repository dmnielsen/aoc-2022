import pytest

from aoc2022 import day_04 as day


@pytest.fixture
def mock_input():
    return """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


@pytest.mark.parametrize('section, range, expected', [[(6, 6), (4, 6), True], [(4, 8), (2, 6), False]])
def test_is_fully_contained(section, range, expected):
    result = day.is_fully_contained(section, range)

    assert expected == result


@pytest.mark.parametrize(
    'section, range, expected',
    [
        [(2, 4), (6, 8), False],
        [(2, 8), (3, 7), False],
        [(3, 7), (2, 8), True],
        [(6, 6), (4, 6), True],
    ],
)
def test_any_overlap(section, range, expected):
    result = day.any_overlap(section, range)
    assert expected == result
    pass


def test_solve_part1(mock_input):
    expected = 2
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 4
    result = day.solve_part2(mock_input)
    assert expected == result
