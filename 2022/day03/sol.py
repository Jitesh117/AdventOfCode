with open('day03/input.txt', 'r') as file:
    data = file.read()

sacks = data.split('\n')

def score(c):
    if 'a' <= c <= 'z':
        return ord(c)-ord('a') + 1
    else:
        return ord(c)-ord('A') + 1 + 26

result_a = 0
for sack in sacks:
    first = sack[:len(sack) // 2]
    second = sack[len(sack)//2:]
    for c in first:
        if c in second:
            result_a += score(c)
            break

print(result_a)

result_b = 0
i = 0
while i < len(sacks):
    for c in sacks[i]:
        if c in sacks[i + 1] and c in sacks[i + 2]:
            result_b += score(c)
            break

    i += 3
print(result_b)