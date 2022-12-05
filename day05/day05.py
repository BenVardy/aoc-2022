from typing import List, Tuple

import re

Ship = List[str]
Instruction = Tuple[int, int, int]


def getoutput(ships: List[Ship]) -> str:
    return ''.join(x[-1] if len(x) > 0 else '' for x in ships)


def part1(ships: List[Ship], ins: List[Instruction]) -> None:
    ships = [x[::] for x in ships]

    for num, _from, to in ins:
        for _ in range(num):
            ships[to].append(ships[_from].pop())

    print(getoutput(ships))


def part2(ships: List[Ship], ins: List[Instruction]) -> None:
    ships = [x[::] for x in ships]

    for num, _from, to in ins:
        fl = len(ships[_from])

        ships[to] += ships[_from][fl - num:]
        ships[_from] = ships[_from][:fl - num]

    print(getoutput(ships))


if __name__ == '__main__':
    f = open('day05/input.txt')
    ship_txt, ins_txt = f.read().split('\n\n')

    crate = re.compile(r'(?:(?:\[([A-Z])\]|   )( |\n))+?', re.MULTILINE)
    ships_re = re.compile(r'\d')

    ships: List[Ship] = [[] for _ in range(len(ships_re.findall(ship_txt)))]

    i = 0
    for c, nl in crate.findall(ship_txt):
        if c != '':
            ships[i].append(c)
        if nl == '\n':
            i = 0
        else:
            i += 1

    ships = [x[::-1] for x in ships]

    ins_re = re.compile(r'move (\d+) from (\d) to (\d)')

    ins: List[Instruction] = [(int(x), int(y) - 1, int(z) - 1)
                              for x, y, z in ins_re.findall(ins_txt)]

    part1(ships, ins)
    part2(ships, ins)
