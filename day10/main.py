# Day 10

from collections import deque

# Question 1
def bfs(puzzle, row, col):
    total = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbours = lambda r, c: [
            (r + y, c + x) for y, x in directions if
            0 <= r + y < len(puzzle) and
            0 <= c + x < len(puzzle[r])]
    queue = deque()
    queue.append((row, col))
    while queue:
        cr, cc = queue.pop()
        for ii, rr in enumerate(puzzle):
            print(''.join([str(k) if (ii, iii) != (cr, cc) else ' ' for iii, k in enumerate(rr)]))
        print()
        value = puzzle[cr][cc]
        print(f"{cr=} {cc=} {value=}")
        if value == 9:
            total += 1
            continue
        for nr, nc in neighbours(cr, cc):
            if puzzle[nr][nc] == value + 1:
                queue.append((nr, nc))
    print(total)
    return total

def question1(puzzle):
    total = 0
    for r, row in enumerate(puzzle):
        for c, cell in enumerate(row):
            if cell == 0:
                value = bfs(puzzle, r, c)
                print(value)
                total += value
    return total

# Question 2
def question2(puzzle):
    total = 0
    return total

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [[int(i) for i in line] for line in inp.read().splitlines()]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 36
    t2, ans2 = question2(sample_input), 0
    assert t1 == ans1, f'S1: {t1} != {ans1}'
    assert t2 == ans2, f'S2: {t2} != {ans2}'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
