with open("input.txt") as file:
    input = file.read()


def part1():
    result = 0
    for line in input.splitlines():
        sides = [int(x) for x in line.split()]
        sides.sort()
        if (sides[0] + sides[1]) > sides[2]:
            result += 1
    print(result)


def part2():
    result = 0
    numbers = []

    for line in input.splitlines():
        numbers.extend([int(x) for x in line.split()])

    for i in range(0, len(numbers), 9):
        group = numbers[i : i + 9]

        for j in range(3):
            triangle = [group[j], group[j + 3], group[j + 6]]
            triangle.sort()
            if (triangle[0] + triangle[1]) > triangle[2]:
                result += 1

    print(result)


part2()
