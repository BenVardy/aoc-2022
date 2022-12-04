from typing import List
import string

Bag = List[str]


def getPriority(x: str) -> int:
    if x in string.ascii_lowercase:
        val = string.ascii_lowercase.index(x) + 1
    else:
        val = string.ascii_uppercase.index(x) + 27

    return val


def part1(bags: List[Bag]) -> None:
    total = 0

    for bag in bags:
        first = set(bag[0:len(bag) // 2])
        second = set(bag[len(bag) // 2::])

        both = (first & second).pop()

        total += getPriority(both)

    print(total)


def part2(bags: List[Bag]) -> None:
    total = 0

    for i in range(0, len(bags), 3):
        bag1, bag2, bag3 = [set(x) for x in bags[i:i + 3]]

        badge = (bag1 & bag2 & bag3).pop()

        total += getPriority(badge)

    print(total)


if __name__ == '__main__':
    f = open('day03/input.txt')
    bags = [list(x.strip()) for x in f.readlines()]

    part1(bags)
    part2(bags)
