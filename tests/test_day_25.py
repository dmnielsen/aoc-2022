import pytest

from aoc2022 import day_25 as day


@pytest.fixture
def mock_input():
    return """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""


@pytest.mark.parametrize(
    'snafu, expected',
    [
        ('1=-0-2', 1747),
        ('12111', 906),
        ('2=0=', 198),
        ('21', 11),
        ('2=01', 201),
        ('111', 31),
        ('20012', 1257),
        ('112', 32),
        ('1=-1=', 353),
        ('1-12', 107),
        ('12', 7),
        ('1=', 3),
        ('122', 37),
        ('2=-1=0', 4890),
    ],
)
def test_snafu2decimal(snafu, expected):
    result = day.snafu2decimal(snafu)
    assert expected == result


@pytest.mark.parametrize(
    'num, expected',
    [
        (1, '1'),
        (2, '2'),
        (3, '1='),
        (4, "1-"),
        (5, '10'),
        (6, '11'),
        (7, '12'),
        (8, '2='),
        (9, '2-'),
        (10, '20'),
        (15, '1=0'),
        (20, '1-0'),
        (2022, '1=11-2'),
        (12345, '1-0---0'),
        (314159265, '1121-1110-1=0'),
        (4890, '2=-1=0'),
    ],
)
def test_decimal2snafu(num, expected):
    result = day.decimal2snafu(num)
    assert expected == result


def test_solve_part1(mock_input):
    expected = '2=-1=0'
    result = day.solve_part1(mock_input)
    assert expected == result
