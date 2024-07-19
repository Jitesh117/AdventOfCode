with open("input.txt") as file:
    input = file.read()
lines = input.splitlines()
codes = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def part1():
    code = ""
    dir_dict = {
        "U": [-1, 0],
        "D": [1, 0],
        "R": [0, 1],
        "L": [0, -1],
    }
    curPos = [1, 1]
    for line in lines:
        for dir in line:
            new_y = curPos[0] + dir_dict[dir][0]
            new_x = curPos[1] + dir_dict[dir][1]
            if 0 <= new_y <= 2 and 0 <= new_x <= 2:
                curPos = [new_y, new_x]
        code += str(codes[curPos[0]][curPos[1]])
    print(code)


part1()

keypad = {
    (0, 2): "1",
    (1, 1): "2",
    (1, 2): "3",
    (1, 3): "4",
    (2, 0): "5",
    (2, 1): "6",
    (2, 2): "7",
    (2, 3): "8",
    (2, 4): "9",
    (3, 1): "A",
    (3, 2): "B",
    (3, 3): "C",
    (4, 2): "D",
}


def part2():
    code = ""
    dir_dict = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1),
    }
    curPos = (2, 0)

    for line in lines:
        for dir in line:
            dy, dx = dir_dict[dir]
            new_y, new_x = curPos[0] + dy, curPos[1] + dx
            if (new_y, new_x) in keypad:
                curPos = (new_y, new_x)
        code += keypad[curPos]

    print(code)


part2()
