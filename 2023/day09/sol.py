with open('2023/day09/input.txt', 'r') as file:
    data = file.read().strip()

lines = data.splitlines()

values = []
for line in lines:
    nums = [int(x) for x in  line.split()]
    values.append(nums)


def solve(arr):
    diff = []
    for i in range(len(arr) - 1):
        diff.append(arr[i+1] - arr[i])
    if all(d == 0 for d in diff):
        return (arr[-1])
    else:
        return (arr[-1] + solve(diff))
        
result_a = 0
result_b = 0
for value in values:
    result_a += solve(value)
    result_b += solve(value[::-1])

print(result_a)
print(result_b)




