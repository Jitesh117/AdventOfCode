with open("./input.txt") as file:
    input = file.read()

lines = input.splitlines()


def part_a(lines):
    dir_map = {"(": 1, ")": -1}
    result = 0
    for line in lines:
        for char in line:
            result += dir_map[char]
    print(result)


def part_b(lines):
    dir_map = {"(": 1, ")": -1}
    result = 0
    for line in lines:
        for index, char in enumerate(line):
            result += dir_map[char]
            if result <= -1:
                print(index + 1)
                break


part_a(lines)
part_b(lines)
