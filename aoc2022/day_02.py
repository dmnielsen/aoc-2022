from pathlib import Path

from typing import List

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202202_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str):
    return [round.split() for round in text.strip().split('\n')]


def score_outcome(opponent: str, you: str) -> int:
    """Assign points for win, lose, draw
    A for Rock, B for Paper, and C for Scissors (opponent)
    X for Rock, Y for Paper, and Z for Scissors (you)

    0 if you lost, 3 if the round was a draw, and 6 if you won
    """
    win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    lose = {'X': 'B', 'Y': 'C', 'Z': 'A'}

    if win[you] == opponent:
        return 6

    elif lose[you] == opponent:
        return 0

    else:
        return 3


def score_shape(shape: str) -> int:
    """Return score for a given shape

    1 for Rock, 2 for Paper, and 3 for Scissors"""
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    return shape_score[shape]


def score_round(round: List[str]) -> int:
    return score_outcome(*round) + score_shape(round[1])


def pick_shape(opponent, outcome) -> str:
    """Given an opponent's shape and required outcome, return shape
    X lose, Y  draw, and Z  win
    A for Rock, B for Paper, and C for Scissors
    """
    win = {'A': 'B', 'B': 'C', 'C': 'A'}
    lose = {'A': 'C', 'B': 'A', 'C': 'B'}

    # Lose
    if outcome == 'X':
        return lose[opponent]
    # Draw
    elif outcome == 'Y':
        return opponent
    # Win
    else:
        return win[opponent]


def solve_part1(input_: str):
    rounds = parse_input(input_)

    return sum(score_round(round) for round in rounds)


def solve_part2(input_: str):
    shape_points = {'A': 1, 'B': 2, 'C': 3}
    outcome_points = {'X': 0, 'Y': 3, 'Z': 6}

    rounds = parse_input(input_)

    return sum(outcome_points[round[1]] + shape_points[pick_shape(*round)] for round in rounds)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
