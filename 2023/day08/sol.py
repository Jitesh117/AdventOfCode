with open('2023/day08/input.txt', 'r') as file:
    data = file.read()


dir,maps = data.split('\n\n')
maps = maps.split('\n')

for i in range(len(maps)):
    maps[i] = maps[i].replace('(','')
    maps[i] = maps[i].replace(')','')

paths = {}
for map in maps:
    first = map.split('=')[0].strip()
    left,right = [(x.strip()) for x in map.split('=')[1].split(', ')]
    paths[first] = [left, right]

result = 0
i = 0

value = 'AAA'
directions = {'L': 0,'R' : 1}
while True:
    if i >= len(dir):
        i = 0
    value = paths[value][directions[dir[i]]]
    i += 1
    result += 1
    if value == 'ZZZ':
        break
print(result)
    
    




