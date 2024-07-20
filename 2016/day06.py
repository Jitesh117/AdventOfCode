from collections import Counter

with open("input.txt") as file:
    input = file.read()
lines = input.splitlines()


def part1():
    columns = list(zip(*lines))
    result = ""
    for col in columns:
        most_common = Counter(col).most_common(1)[0][0]
        result += most_common
    print(result)


def part2():
    columns = list(zip(*lines))
    result = ""
    for col in columns:
        least_common = Counter(col).most_common()[-1][0]
        result += least_common
    print(result)


part1()
part2()
