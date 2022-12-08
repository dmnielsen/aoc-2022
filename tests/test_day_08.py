import numpy as np
import pytest

from aoc2022 import day_08 as day


@pytest.fixture
def mock_input():
    return """30373
25512
65332
33549
35390"""


@pytest.fixture
def mock_array():
    return np.array([[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]])


def test_calculate_scenic_score(mock_array):
    loc = (3, 2)
    expected = 8

    result = day.calculate_scenic_score(loc, mock_array)
    assert expected == result


def test_solve_part1(mock_input):
    expected = 21
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 8
    result = day.solve_part2(mock_input)
    assert expected == result
