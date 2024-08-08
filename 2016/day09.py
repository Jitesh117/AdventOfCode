import re


def part1(s):
    result = 0
    i = 0
    while i < len(s):
        if s[i] == "(":
            match = re.search(r"\((\d+)x(\d+)\)", s[i:])
            if match:
                chars, times = map(int, match.groups())
                end = i + match.end()
                result += chars * times
                i = end + chars
            else:
                result += 1
                i += 1
        else:
            result += 1
            i += 1
    return result


def part2(s):
    if "(" not in s:
        return len(s)

    result = 0
    i = 0
    while i < len(s):
        if s[i] == "(":
            match = re.search(r"\((\d+)x(\d+)\)", s[i:])
            if match:
                chars, times = map(int, match.groups())
                end = i + match.end()
                result += times * part2(s[end : end + chars])
                i = end + chars
            else:
                result += 1
                i += 1
        else:
            result += 1
            i += 1
    return result


# Example usage
with open("input.txt") as file:
    input = file.read()
print("Part 1:", sum(part1(line) for line in input.splitlines()))
print("Part 2:", sum(part2(line) for line in input.splitlines()))
