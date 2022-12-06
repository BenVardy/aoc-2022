def part1(_in: str) -> None:
    for i in range(0, len(_in) - 4):
        valid = True
        for x in _in[i:i + 4]:
            if _in[i:i + 4].count(x) > 1:
                valid = False
                break

        if valid:
            print(i + 4)
            break


def part2(_in: str) -> None:
    for i in range(0, len(_in) - 14):
        valid = True
        for x in _in[i:i + 14]:
            if _in[i:i + 14].count(x) > 1:
                valid = False
                break

        if valid:
            print(i + 14)
            break


if __name__ == '__main__':
    f = open('day06/input.txt')
    line = f.readline().strip()

    part1(line)
    part2(line)
