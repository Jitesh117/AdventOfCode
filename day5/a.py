with open('day5/input.txt', 'r') as file:
    data = file.read()
maps = data.split('\n')

sections = data.split('\n\n')
seeds, *function_data = sections
seeds = [int(x) for x in seeds.split(':')[1].split()]

class Operations:
    def __init__(self, set_str):
        maps = set_str.split('\n')[1:]  
        self.instructions: list[tuple[int, int, int]] = [
            [int(x) for x in line.split()]
            for line in maps
        ]
        
    def apply_one(self, value: int) -> int:
        for (destination, source, size) in self.instructions:
            if source <= value < source + size:
                return value + destination - source
        return value

    def apply_range(self, ranges):
        applied = []
        for (dest, src, sz) in self.instructions:
            src_end = src + sz
            new_ranges = []
            while ranges:
                (start, end) = ranges.pop()
                before = (start, min(end, src))
                intersect = (max(start, src), min(src_end, end))
                after = (max(src_end, start), end)
                if before[1] > before[0]:
                    new_ranges.append(before)
                if intersect[1] > intersect[0]:
                    applied.append((intersect[0] - src + dest, intersect[1] - src + dest))
                if after[1] > after[0]:
                    new_ranges.append(after)
            ranges = new_ranges
        return applied + ranges

functions = [Operations(data) for data in function_data]

P1_results = []
for value in seeds:
    for function in functions:
        value = function.apply_one(value)
    P1_results.append(value)
print(min(P1_results))

P2_results = []
pairs = list(zip(seeds[::2], seeds[1::2]))
for start, size in pairs:
    ranges = [(start, start + size)]
    for function in functions:
        ranges = function.apply_range(ranges)
    P2_results.append(min(ranges)[0])
print(min(P2_results))
