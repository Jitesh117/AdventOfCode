from collections import defaultdict
with open('day5/input.txt', 'r') as file:
    input_text = file.read()

parts = input_text.split('\n\n')

seeds = parts[0].split(':')[1].split()
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

maps = []
for i in range(1, len(parts)):
    item_list = []
    for item in parts[i].split('\n')[1:]:
        items = item.split()
        item_int = [int(cur_item) for cur_item in items]
        item_list.append(item_int)
    maps.append(item_list)


list_of_lists = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

# Using nested list comprehension to convert strings to integers
# for i in range(len(maps)):
#     for j in range(len(maps[i])):
#         for k in range(len(maps[i][j])):
#             maps[i][j][k] = int(maps[i][j][k])

# for map in maps:
#     for item in map:
#         print(item)
#     print()

dicts = []
i = 0
for map in maps:
    cur_dict = {}
    for list in map:
        dest = list[0]
        source = list[1]
        range_len = list[2]
        print(dest, source, range_len)
        for i in range(range_len):
            cur_dict[source] = dest
            source = source + 1
            dest = dest + 1
    dicts.append(cur_dict)

result = 2 ** 1000
i = 0

for seed in seeds:
    print(i)

    value = seed
    for dict in dicts:
        if value in dict:
            value = dict[value]
    result = min(result, value)

print(result)

