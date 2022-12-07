import pytest

from aoc2022 import day_06 as day


@pytest.fixture
def mock_input():
    return """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""


@pytest.mark.parametrize(
    'text, expected',
    [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
    ],
)
def test_solve_part1(text, expected):
    result = day.solve_part1(text)
    assert expected == result


@pytest.mark.parametrize(
    'text, expected',
    [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
    ],
)
def test_solve_part2(text, expected):
    result = day.solve_part2(text)
    assert expected == result
