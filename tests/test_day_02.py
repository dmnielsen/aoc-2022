import pytest

from aoc2022 import day_02 as day


@pytest.fixture
def mock_input():
    return """A Y
B X
C Z"""


def test_parse_input(mock_input):
    expected = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
    result = day.parse_input(mock_input)
    assert all([(choice == result[i][j]) for i, round in enumerate(expected) for j, choice in enumerate(round)])


@pytest.mark.parametrize('round,expected', [(('A', 'Y'), 6), (('B', 'X'), 0), (('C', 'Z'), 3)])
def test_score_outcome(round, expected):
    result = day.score_outcome(*round)
    assert result == expected


@pytest.mark.parametrize('round,expected', [(('A', 'Y'), 8), (('B', 'X'), 1), (('C', 'Z'), 6)])
def test_score_round(round, expected):
    result = day.score_round(round)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 15
    result = day.solve_part1(mock_input)
    assert expected == result


@pytest.mark.parametrize('round,expected', [(('A', 'Y'), 'A'), (('B', 'X'), 'A'), (('C', 'Z'), 'A')])
def test_pick_shape(round, expected):
    result = day.pick_shape(*round)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 12
    result = day.solve_part2(mock_input)
    assert expected == result
