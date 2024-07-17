import re

import numpy as np

with open("input.txt") as file:
    input = file.read()

lines = input.splitlines()

grid = np.full((1000, 1000), False)

for i in lines:
    coord = [int(a) for a in re.findall(r"\d+", i)]
    if coord:
        x_i, y_i, x_f, y_f = coord
        if i.startswith("turn on"):
            grid[x_i : x_f + 1, y_i : y_f + 1] = True
        elif i.startswith("turn off"):
            grid[x_i : x_f + 1, y_i : y_f + 1] = False
        elif i.startswith("toggle"):
            grid[x_i : x_f + 1, y_i : y_f + 1] = ~grid[x_i : x_f + 1, y_i : y_f + 1]

print((grid == True).sum())

grid = np.zeros((1000, 1000))

for i in lines:
    coord = [int(a) for a in re.findall(r"\d+", i)]
    if coord:
        x_i, y_i, x_f, y_f = coord
        if i.startswith("turn on"):
            grid[x_i : x_f + 1, y_i : y_f + 1] += 1
        elif i.startswith("turn off"):
            grid[x_i : x_f + 1, y_i : y_f + 1] -= 1
            grid = grid.clip(0)
        elif i.startswith("toggle"):
            grid[x_i : x_f + 1, y_i : y_f + 1] += 2

print(int(np.sum(grid)))
