with open('day01/input.txt', 'r') as file:
    data = file.read()

elves = [l.strip() for l in open('day01/input.txt')]

calories = []
for elf in ('\n'.join(elves)).split('\n\n'):
    calorie = 0
    for x in elf.split('\n'):
        calorie += int(x)
    calories.append(calorie)
calories = sorted(calories)
print(calories[-1])
print(calories[-1]+calories[-2]+calories[-3])