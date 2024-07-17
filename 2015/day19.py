import re

with open("input.txt") as file:
    input = file.read()
lines = input.splitlines()

replacements = []
for i in lines[:-2]:
    m = re.findall(r'(\S+) => (\S+)', i)
    replacements.append(m[0])

X = lines[-1]

result = set()
for i, j in replacements:
    for k in range(len(X)):
        if X[k : k + len(i)] == i:
            y = X[:k] + j + X[k + len(i):]
            result.add(y)
print(len(result))

