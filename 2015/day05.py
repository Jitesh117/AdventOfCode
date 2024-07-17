import re


with open("input.txt") as file:
    input = file.read()

lines = input.splitlines()


def is_nice_string(string):
    condition1 = r"(?=.*[aeiou].*[aeiou].*[aeiou])"
    condition2 = r"(\w)(\1)"
    condition3 = r"(?!.*ab)(?!.*cd)(?!.*pq)(?!.*xy)"

    regex = condition3 + condition1 + condition2
    return bool(re.search(regex, string))


def part1(lines):
    result = 0
    for line in lines:
        result += int(is_nice_string(line))
    print(result)


def solve(string):
    condition1 = r"((\w\w).*\2)"

    condition2 = r"(\w).\1"

    # Check if both conditions are satisfied
    return bool(re.search(condition1, string)) and bool(re.search(condition2, string))


def part2(lines):
    result = 0
    for line in lines:
        result += int(solve(line))
    print(result)


part1(lines)
part2(lines)
