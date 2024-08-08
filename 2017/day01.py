def part1(sequence: str) -> int:
    result = 0
    length = len(sequence)

    for i in range(length):
        if sequence[i] == (sequence[(i + 1) % length]):
            result += int(sequence[i])
    return result


def part2(sequence: str) -> int:
    result = 0
    length = len(sequence)

    for i in range(length):
        if sequence[i] == sequence[(i + length // 2) % length]:
            result += int(sequence[i])

    return result


if __name__ == "__main__":
    input = open("input.txt").read().strip()
    print("part 1: ", part1(input))
    print("part 2: ", part2(input))
