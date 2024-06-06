import re

with open("input.txt") as file:
    data = file.read()
LINES = data.splitlines()

pattern = re.compile('^([a-zA-Z]+) would (lose|gain) ([0-9]+) happiness units by sitting next to ([a-zA-Z]+).')

names = set(l.split(' ')[0] for l in LINES)
happiness = {}
for outer in names:
    for inner in names:
        if inner != outer:
            happiness[frozenset((outer, inner))] = 0

for l in LINES:
    outer, status, measure, inner = pattern.match(l).groups()
    measure = int(measure)
    if status == 'lose':
        measure *= -1
    happiness[frozenset((outer, inner))] += measure

def optimize(remainder, current, end):
    if len(remainder) == 0:
        return happiness[frozenset((current, end))]
    result = -99999999
    for next in remainder:
        result = max(result, happiness[frozenset((current, next))] + optimize(remainder.difference({next}), next, end))
    return result

start = names.pop()
answer1 = optimize(names, start, start)

print(answer1)

names.add(start)
for name in names:
    happiness[frozenset(('me', name))] = 0
names.add('me')

start = names.pop()
answer2 = optimize(names, start, start)
print(answer2)