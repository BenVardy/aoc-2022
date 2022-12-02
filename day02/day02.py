from typing import List, Tuple

Input = List[Tuple[str, str]]

points = {
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3,  # Scissors
}


def rps1(c: Tuple[str, str]) -> int:
    oC = {'A': 'R', 'B': 'P', 'C': 'S'}
    oM = {'X': 'R', 'Y': 'P', 'Z': 'S'}
    winners = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
    if c in winners:
        return 6
    elif oC[c[0]] == oM[c[1]]:
        return 3
    else:
        return 0


def part1(_in: Input) -> None:
    total = 0
    for x in _in:
        total += points[x[1]] + rps1(x)

    print(total)


def rps2(move: str, wtd: str) -> int:
    win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}

    if wtd == 'X':  # Lose
        return points[lose[move]]
    elif wtd == 'Y':  # draw
        return points[draw[move]] + 3
    else:
        return points[win[move]] + 6


def part2(_in: Input) -> None:
    total = 0
    for x in _in:
        total += rps2(x[0], x[1])

    print(total)


if __name__ == '__main__':
    f = open('day02/input.txt')
    _input = [tuple(x.strip().split(' ')) for x in f.readlines()]

    part1(_input)
    part2(_input)
