with open("input.txt") as file:
    input = file.read()
steps = input.strip().split(", ")


def part1():
    x = 0
    y = 0

    for step in steps:
        if step[0] == "R":
            x, y = -y, x
        else:
            x, y = y, -x

        x += int(step[1:])

    print(abs(x) + abs(y))


def part2():
    x = 0
    y = 0
    dx, dy = 0, 1  # Start facing north
    visited = set([(0, 0)])  # Set to store visited locations

    for step in steps:
        turn = step[0]
        distance = int(step[1:])

        # Turn
        if turn == "R":
            dx, dy = dy, -dx
        else:  # turn == "L"
            dx, dy = -dy, dx

        # Move and check each step
        for _ in range(distance):
            x += dx
            y += dy
            if (x, y) in visited:
                print(abs(x) + abs(y))
                return
            visited.add((x, y))

    print("No location visited twice")


# Assuming 'steps' is defined elsewhere in your code
part1()
part2()
