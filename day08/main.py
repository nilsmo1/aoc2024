# Day 8

from collections import defaultdict
from itertools import combinations

# Question 1
def question1(puzzle):
    ymax, xmax, frequencies = puzzle
    anti_nodes = set()
    for frequency, positions in frequencies.items():
        for (y1, x1), (y2, x2) in combinations(positions, 2):
            dy = abs(y1 - y2)
            dx = abs(x1 - x2)
            dx *= -1 if x1 < x2 else 1
            upper = (y1 - dy, x1 + dx)
            lower = (y2 + dy, x2 - dx)
            anti_nodes.add(upper)
            anti_nodes.add(lower)
    return sum(1 for y, x in anti_nodes if 0 <= y < ymax and 0 <= x < xmax)

# Question 2
def question2(puzzle):
    ymax, xmax, frequencies = puzzle
    anti_nodes = set()
    for frequency, positions in frequencies.items():
        for (y1, x1), (y2, x2) in combinations(positions, 2):
            dy = abs(y1 - y2)
            dx = abs(x1 - x2)
            dx *= -1 if x1 < x2 else 1
            while (0 <= y1 - dy < ymax and 0 <= x1 + dx < xmax):
                upper = (y1 - dy, x1 + dx)
                anti_nodes.add(upper)
                y1 -= dy
                x1 += dx
            while (0 <= y2 + dy < ymax and 0 <= x2 - dx < xmax):
                lower = (y2 + dy, x2 - dx)
                anti_nodes.add(lower)
                y2 += dy
                x2 -= dx
    return sum(1 for y, x in anti_nodes if 0 <= y < ymax and 0 <= x < xmax)

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        frequencies = defaultdict(list)
        split_file = inp.read().splitlines()
        ymax, xmax = len(split_file), len(split_file[0])
        for i, line in enumerate(split_file):
            for j, c in enumerate(line):
                if c.isdigit() or c.isalpha():
                    frequencies[c].append((i, j))
        return ymax, xmax, frequencies

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 14
    t2, ans2 = question2(sample_input), 34
    assert t1 == ans1, f'S1: {t1} != {ans1}'
    assert t2 == ans2, f'S2: {t2} != {ans2}'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
