def part1(lines):
    result = 0

    for line in lines:
        num_list = [int(x) for x in line.split()]
        max_num = max(num_list)
        min_num = min(num_list)
        result += max_num - min_num
    return result


def part2(lines):
    int_lines = [[int(x) for x in line.split()] for line in lines]
    result = 0
    for line in int_lines:
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if line[i] % line[j] == 0:
                    result += line[i] // line[j]
                elif line[j] % line[i] == 0:
                    result += line[j] // line[i]
    return result


if __name__ == "__main__":
    input = open("input.txt").read()
    lines = input.splitlines()
    print(part1(lines))
    print(part2(lines))
