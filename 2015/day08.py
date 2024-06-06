import re

with open("input.txt") as file:
    data = file.read()

lines = data.splitlines()
result = 0
for line in lines:
    code = len(line)
    memory = len(line.encode("utf-8").decode('unicode-escape')) - 2
    result += code - memory
print(result)

code = sum([len(x) for x in lines])
extended = sum([len(re.sub('"', '"\"', repr(x))) for x in lines])

print(extended - code)