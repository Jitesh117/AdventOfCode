def calculate_paper(l, w, h):
    sides = [l * w, w * h, h * l]
    return 2 * sum(sides) + min(sides)


def calculate_ribbon(l, w, h):
    perimeters = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
    return min(perimeters) + l * w * h


def solve_day2(input_file):
    total_paper = 0
    total_ribbon = 0

    with open(input_file, "r") as file:
        for line in file:
            l, w, h = map(int, line.strip().split("x"))
            total_paper += calculate_paper(l, w, h)
            total_ribbon += calculate_ribbon(l, w, h)

    return total_paper, total_ribbon


# Solve the puzzle
input_file = "input.txt"  # Replace with your input file path
paper, ribbon = solve_day2(input_file)

print(f"Part 1: {paper}")
print(f"Part 2: {ribbon}")
