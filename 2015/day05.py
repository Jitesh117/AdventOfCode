import re

with open("input.txt") as file:
    input = file.read()

lines = input.splitlines()

result = 0
disallowed = ['ab', 'cd', 'pq', 'xy']

def part1(lines):
    for line in lines:
        vowel = 0
        present = False
        repeat = False
        line += "*"
        for word in disallowed:
            if word in line:
                present = True
                break

        for i in range(len(line) - 1):
            if line[i] in "aeiou":
                vowel += 1
            if line[i] == line[i + 1]:
                repeat = True
        if vowel >= 3 and  (not present) and repeat:
            result += 1

    print(result)

naughty = 0

for s in lines:
    if re.match(r"\w*(\w\w)\w*\1\w*", s) is None:
        naughty += 1
    elif re.match(r"\w*(\w)[^\1]\1\w*", s) is None:
        naughty +=1
        
print(len(lines)-naughty)