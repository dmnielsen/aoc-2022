import pytest

from aoc2022 import day_20 as day


@pytest.fixture
def mock_input():
    return """1
2
-3
3
-2
0
4"""


progression = [
    [0, 1, 2, 3, 4, 5, 6],
    [1, 0, 2, 3, 4, 5, 6],
    [0, 2, 1, 3, 4, 5, 6],
    [0, 1, 3, 4, 2, 5, 6],
    [0, 1, 4, 2, 5, 3, 6],
    [0, 1, 2, 5, 3, 6, 4],
    [0, 1, 2, 5, 3, 6, 4],
    [0, 1, 2, 6, 5, 3, 4],
]


@pytest.mark.parametrize(
    'idx, val, positions, expected',
    [
        (0, 1, progression[0], progression[1]),
        (1, 2, progression[1], progression[2]),
        (2, -3, progression[2], progression[3]),
        (3, 3, progression[3], progression[4]),
        (4, -2, progression[4], progression[5]),
        (5, 0, progression[5], progression[6]),
        (6, 4, progression[6], progression[7]),
    ],
)
def test_move_index(idx, val, positions, expected):
    result = day.move_index(idx, val, positions)
    assert all([v == result[i] for i, v in enumerate(expected)])


def test_solve_part1(mock_input):
    expected = 3
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 1623178306
    result = day.solve_part2(mock_input)
    assert expected == result
