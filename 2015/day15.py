import functools
import itertools
import re


def generate_weights(n):
    for t in itertools.combinations_with_replacement(range(101), n):
        if sum(t) == 100:
            yield from itertools.permutations(t)

with open('input.txt') as f:
    inp = f.readlines()

ing = []

for i in inp:
    args = re.search(r'capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$', i.rstrip()).groups()
    vals = map(int, args)
    ing.append(tuple(vals))
    
p1 = -1
p2 = -1
for weights in generate_weights(len(ing)):
    tot = [0, 0, 0, 0, 0]
    for i, item in enumerate(ing):
        for j, prop in enumerate(item):
            tot[j] += weights[i] * prop
    score = functools.reduce(lambda x,y: max(x,0)*max(y,0), tot[:-1])
    p1 = max(p1, score)
    p2 = max(p2, int(tot[-1] == 500) * score)

print(p1)
print(p2)