with open('2022/day10/input.txt', 'r') as file:
    data = file.read()

lines = data.split('\n')
value = 1
cycle = 0
result = 0

def solveCycle(cycle, value):
    global result
    if cycle in [20, 60, 100, 140, 180, 220]:
        print(cycle)
        result += cycle * value

for line in lines:
    words = line.split()
    if words[0] == 'noop':
        cycle += 1
        solveCycle(cycle,value)
    elif words[0] == 'addx':
        cycle += 1
        solveCycle(cycle,value)
        cycle += 1
        solveCycle(cycle,value)
        value += int(words[1])

print(result)

