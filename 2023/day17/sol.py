#!/bin/python3

from heapq import heappop, heappush
import sys
from typing import List

FILE = "2023/day17/input.txt"


def read_lines_to_list() -> List[int]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append([int(val) for val in list(line)])

    return lines


NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)


def neighbours(maze: List[List[str]], curr, ultra: bool):
    max_moves = 3
    if ultra:
        max_moves = 10

    min_moves = None
    if ultra:
        min_moves = 4

    height = len(maze)
    width = len(maze[0])
    (y, x, direction, direction_moves) = curr

    res = []

    for new_direction in [NORTH, EAST, SOUTH, WEST]:
        (new_y, new_x) = (y + new_direction[0], x + new_direction[1])

        if not (new_y >= 0 and new_x >= 0 and new_y < height and new_x < width):
            continue

        if direction == new_direction:
            new_direction_moves = direction_moves + 1
        else:
            new_direction_moves = 1

        # Max move condition
        if new_direction_moves > max_moves:
            continue

        # If there is one, min move condition
        if min_moves and direction != new_direction and direction_moves < min_moves:
            continue

        # No reversing
        if (new_direction[0] * -1, new_direction[1] * -1) == direction:
            continue

        res.append((new_y, new_x, new_direction, new_direction_moves))

    return res


def dijkstra(maze: List[List[int]], ultra: bool) -> int:
    height = len(maze)
    width = len(maze[0])
    start = (0, 0)
    end = (height - 1, width - 1)

    distances = dict()

    # Of the form cost -> y, x, direction, distance in that direction
    pq = []

    for direction in [EAST, SOUTH]:
        heappush(pq, (0, (*start, direction, 0)))

    while pq:
        (cost, curr) = heappop(pq)
        if curr in distances:
            continue

        distances[curr] = cost

        for neighbour in neighbours(maze, curr, ultra):
            if neighbour not in distances or new_cost < distances[curr]:
                new_cost = cost + maze[neighbour[0]][neighbour[1]]
                heappush(pq, (new_cost, neighbour))

    return min(
        [
            val
            for ((y, x, _dir, dir_move), val) in distances.items()
            if (y, x) == end and (not ultra or dir_move >= 4)
        ]
    )


def part_one():
    maze = read_lines_to_list()
    answer = dijkstra(maze, False)

    print(f"Part 1: {answer}")


def part_two():
    maze = read_lines_to_list()
    answer = dijkstra(maze, True)

    print(f"Part 2: {answer}")


part_one()
part_two()
