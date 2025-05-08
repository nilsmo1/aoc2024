# Day 11

# Question 1
def question1(puzzle):
    total = 0
    p = [int(s) for s in puzzle]
    step = 0
    stone = 0
    while step != 25:
        if not p[stone]:
            p[stone] = 1
        elif len(str(p[stone])) % 2 == 0:
            p.insert
    return total

# Question 2
def question2(puzzle):
    total = 0
    return total

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return inp.read().strip().split()

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 55312
    t2, ans2 = question2(sample_input), 0
    assert t1 == ans1, f'S1: {t1} != {ans1}'
    assert t2 == ans2, f'S2: {t2} != {ans2}'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
