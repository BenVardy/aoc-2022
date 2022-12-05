from typing import List, Tuple

Range = Tuple[int, int]
Pair = Tuple[Range, Range]


def part1(pairs: List[Pair]) -> None:
    total = 0
    for p1, p2 in pairs:
        p1s, p1e = p1
        p2s, p2e = p2

        # p1 in p2.
        if p2s <= p1s and p2e >= p1e:
            total += 1
        # p2 in p1.
        elif p1s <= p2s and p1e >= p2e:
            total += 1

    print(total)


def part2(pairs: List[Pair]) -> None:
    total = 0
    for p1, p2 in pairs:
        p1a = set(range(p1[0], p1[1] + 1))
        p2a = set(range(p2[0], p2[1] + 1))

        if len(p1a & p2a) != 0:
            total += 1

    print(total)


if __name__ == '__main__':
    f = open('day04/input.txt')
    pairs = [
        tuple(
            tuple(int(z) for z in y.split('-')) for y in x.strip().split(','))
        for x in f.readlines()
    ]

    part1(pairs)
    part2(pairs)
