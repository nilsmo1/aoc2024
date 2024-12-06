# Day 6

# Question 1
def get_start(puzzle):
    for i, row in enumerate(puzzle):
        for j, char in enumerate(row):
            if char == '^':
                return i, j

def question1(puzzle):
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
    return len(visited)

# Question 2
def question2(puzzle):
    total = 0
    return total

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [line for line in inp.read().splitlines()]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 41
    t2, ans2 = question2(sample_input), 0
    assert t1 == ans1, f'S1: {t1} != {ans1}'
    assert t2 == ans2, f'S2: {t2} != {ans2}'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
