with open('day06/input.txt', 'r') as file:
    data = file.read()

times = [int(x) for x in data.split('\n')[0].split(': ')[1].split()]
distances = [int(x) for x in data.split('\n')[1].split(': ')[1].split()]

result_a = 1
n = len(times)

for i in range(n):
    count = 0
    for j in range(times[i]):
        dist = (j * (times[i] - j))
        if dist > distances[i]:
            count += 1
    result_a *= count
print(result_a)

time = data.split('\n')[0].split(': ')[1].split()
distance = data.split('\n')[1].split(': ')[1].split()

times = ""
distances = ""
for t in time:
    times += t
for d in distance:
    distances += d
times = int(times)
distances = int(distances)
result_b = 1
count = 0
for j in range(times):
    dist = (j * (times - j))
    if dist > distances:
        count += 1
result_b *= count

# print(result_b)


