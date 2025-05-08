# Day 9

# Question 1
def question1(puzzle):
    l = []
    if len(puzzle) % 2:
        puzzle.append(0)
    for idx, i in enumerate(range(0, len(puzzle) - 1, 2)):
        first, second = puzzle[i], puzzle[i+1]
        for _ in range(first):
            l.append(idx)
        for _ in range(second):
            l.append(-1)
    L = len(l) - 1
    R = 0
    while R < L:
        if l[L] < 0:
            L -= 1
        if l[R] < 0:
            l[R] = l[L]
            l[L] = -1
            L -= 1
        R += 1
    print(''.join([str(i) if i >= 0 else '.' for i in l]))
    print(l[R])
    print(l[R] == -1)
    print()
    l = l[:R+1]
    return sum(i * n for i, n in enumerate(l))

# Question 2
def question2(puzzle):
    total = 0
    return total

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [int(i) for i in inp.read().strip()]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 1928
    exit()
    t2, ans2 = question2(sample_input), 0
    assert t1 == ans1, f'S1: {t1} != {ans1}'
    assert t2 == ans2, f'S2: {t2} != {ans2}'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
