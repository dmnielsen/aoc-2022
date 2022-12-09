import pytest

from aoc2022 import day_09 as day


@pytest.fixture
def mock_input():
    return """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


@pytest.mark.parametrize(
    'h, t, expected',
    [
        ((1, 1), (1, 1), True),
        ((2, 3), (1, 2), True),
        ((1, 2), (2, 3), True),
        ((1, 2), (0, 0), False),
        ((5, 5), (4, 5), True),
        ((5, 5), (6, 5), True),
    ],
)
def test_is_touching(h, t, expected):
    result = day.is_touching(h, t)
    assert expected == result


def test_solve_part1(mock_input):
    expected = 13
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 1
    result = day.solve_part2(mock_input)
    assert expected == result


@pytest.fixture
def mock_input_larger():
    return """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def test_solve_part2_larger_example(mock_input_larger):
    expected = 36
    result = day.solve_part2(mock_input_larger)
    assert expected == result
