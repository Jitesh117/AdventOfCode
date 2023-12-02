
from collections import defaultdict
with open('input.txt', 'r') as file:
    input_text = file.read()

result = 0

for line in input_text.split('\n'):
	ok = True
	id_, line = line.split(':')
	V = defaultdict(int)
	for event in line.split(';'):
		for balls in event.split(','):
			n,color = balls.split()
			n = int(n)
			V[color] = max(V[color], n)
			if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
				ok = False
	score = 1
	for v in V.values():
		score *= v
	result += score
print(result)

