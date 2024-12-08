# Day 6

from copy import deepcopy
from collections import defaultdict

# Question 1
def get_start(puzzle):
    for i, row in enumerate(puzzle):
        for j, char in enumerate(row):
            if char == '^':
                return i, j

def get_visited(puzzle):
    y, x = get_start(puzzle)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0
    in_bounds = lambda r, c: 0 <= r < len(puzzle) and 0 <= c < len(puzzle[r])
    visited = set()
    while in_bounds(y, x):
        visited.add((y, x))
        dy, dx = directions[direction]
        if not in_bounds(y + dy, x + dx):
            break
        if puzzle[y + dy][x + dx] == '#':
            direction += 1
            direction %= len(directions)
            continue
        y += dy
        x += dx
    return visited

def question1(puzzle):
    return len(get_visited(puzzle))

# Question 2
def question2(puzzle):
    total = 0
    already_visited = get_visited(puzzle)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    in_bounds = lambda r, c: 0 <= r < len(puzzle) and 0 <= c < len(puzzle[r])
    for i, j in already_visited:
        y, x = get_start(puzzle)
        if puzzle[i][j] == '^' or puzzle[i][j] == '#':
            continue
        direction = 0
        visited = defaultdict(int)
        while in_bounds(y, x):
            visited[(y, x, direction)] += 1
            dy, dx = directions[direction]
            if not in_bounds(y + dy, x + dx):
                break
            if puzzle[y + dy][x + dx] == '#' or (y + dy, x + dx) == (i, j):
                if visited[(y, x, direction)] > 2:
                    total += 1
                    break
                direction += 1
                direction %= len(directions)
                continue
            y += dy
            x += dx
    return total

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [[char for char in line] for line in inp.read().splitlines()]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 41
    t2, ans2 = question2(sample_input), 6
    assert t1 == ans1, f'S1: {t1} != {ans1}'
    assert t2 == ans2, f'S2: {t2} != {ans2}'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
