import re
from collections import deque
from collections.abc import Collection
from copy import deepcopy
from functools import cached_property
from itertools import permutations
from pathlib import Path
from typing import Any, Optional, Union

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202216_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


class Tunnel:
    def __init__(self, name, rate: int, neighbors: Collection[str]):
        self.name = name
        self.rate = rate
        self.neighbors = neighbors

        self.cost = float('inf')

        self._steps: dict[str, int] = {}

    def __repr__(self):
        return f"Tunnel(name={self.name}, rate={self.rate}, neighbors={self.neighbors})"

    @property
    def steps_to_other_tunnels(self):
        return self._steps

    @steps_to_other_tunnels.setter
    def steps_to_other_tunnels(self, step_dict: dict[str, int]):
        self._steps = step_dict

    def add_tunnel_to_steps(self, other: str, n_steps: int):
        self._steps[other] = n_steps
#
#
# class Path:
#     def __init__(self, start: Union[Tunnel, Path], end: Union[Tunnel, Path]):
#         self.start = start
#         self.end = end
#
#     @cached_property
#     def tunnels(self) -> list[Tunnel]:
#         tunnels = []
#         if isinstance(self.start, Path):
#             tunnels.extend(self.start.tunnels)
#         else:
#             tunnels = [self.start]
#
#         if isinstance(self.end, Path):
#             tunnels.extend(self.end.tunnels)
#         else:
#             tunnels.append(self.end)
#         return tunnels
#
#     @cached_property
#     def end_rate(self) -> int:
#         rate = 0
#         if isinstance(self.start, Path):
#             rate += self.start.end_rate
#         else:
#             rate += self.start.rate
#
#         if isinstance(self.end, Path):
#             rate += self.end.end_rate
#         else:
#             rate += self.end.rate
#         return rate
#
#     @cached_property
#     def time_elapsed(self) -> int:
#         if isinstance(self.start, Path) and isinstance(self.end, Path):
#             return self.start.time_elapsed + self.end.time_elapsed
#         elif isinstance(self.start, Tunnel) and isinstance(self.end, Tunnel):
#             return self.end.steps_to_other_tunnels[self.start.name]
#         elif isinstance(self.start, Path):
#             return self.end.steps_to_other_tunnels[self.start.tunnels[-1].name]
#         elif isinstance(self.end, Path):
#             return self.start.steps_to_other_tunnels[self.end.tunnels[0].name]
#         else:
#             return 0
#
#     @cached_property
#     def released(self) -> int:
#
#         return 0


def parse_input(text: str) -> Collection[Tunnel]:
    p = re.compile(r'Valve (\w\w) .* rate=([0-9]+); .*to valve[s]* (.*)')
    raw = p.findall(text)

    tunnel_dict = {}
    for line in raw:
        tunnel_id, rate, connections = line
        tunnel_dict[tunnel_id] = Tunnel(tunnel_id, int(rate), connections.split(', '))
    return tunnel_dict


def get_non_zero_flow_rate_tunnels(tunnels: dict[str, Tunnel]):
    non_zero = [(name, tunnel.rate) for name, tunnel in tunnels.items() if tunnel.rate > 0]
    return sorted(non_zero, key=lambda x: x[1], reverse=True)


def get_lowest_cost_node(unprocessed: dict[str, int], processed: set) -> Optional[str]:
    for tunnel, cost in sorted(unprocessed.items(), key=lambda x: x[1]):
        if tunnel not in processed:
            return tunnel
    return None


def find_time_to_other_tunnels(start: str, tunnels: dict[str, Tunnel]):
    tunnels = deepcopy(tunnels)
    minutes_to_tunnels: dict[str, int] = {}

    tunnels[start].cost = 0

    processed: set[str] = set()
    unprocessed_with_cost = {start: 0}
    check_tunnel = get_lowest_cost_node(unprocessed_with_cost, processed)
    # breakpoint()
    while check_tunnel is not None:

        tunnel_info = tunnels[check_tunnel]
        new_cost = tunnel_info.cost + 1
        for t in tunnel_info.neighbors:
            if new_cost < tunnels[t].cost:
                tunnels[t].cost = new_cost
                if t not in processed:
                    minutes_to_tunnels[t] = new_cost
                    unprocessed_with_cost[t] = new_cost
        processed.update([check_tunnel])
        check_tunnel = get_lowest_cost_node(unprocessed_with_cost, processed)

    return minutes_to_tunnels


def populate_times_to_other_tunnels(tunnels):
    for tunnel, obj in tunnels.items():
        obj.steps_to_other_tunnels = find_time_to_other_tunnels(tunnel, tunnels)


def solve_part1(input_: str):
    tunnels = parse_input(input_)

    for tunnel, obj in tunnels.items():
        obj.steps_to_other_tunnels = find_time_to_other_tunnels(tunnel, tunnels)

    non_zero = get_non_zero_flow_rate_tunnels(tunnels)

    return


def solve_part2(input_: str):
    return


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
