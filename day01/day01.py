from typing import List


def part1(elves: List[List[int]]):
    print(max(sum(x) for x in elves))


def part2(elves: List[List[int]]):
    print(sum(sorted((sum(x) for x in elves), reverse=True)[:3]))


if __name__ == '__main__':
    f = open('day01/input.txt')

    elves = [[int(y) for y in x.strip().split('\n')]
             for x in f.read().strip().split('\n\n')]

    part1(elves)
    part2(elves)
