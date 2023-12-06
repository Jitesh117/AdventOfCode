with open('day04/input.txt', 'r') as file:
    data = file.read()

lines = data.split('\n')

result_a = 0
result_b = 0

for line in lines:
    one, two = line.split(',')
    s1, e1= one.split('-')
    s2, e2= two.split('-')
    s1, e1, s2, e2 = [int(x) for x in [s1 , e1, s2, e2]]

    if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
        result_a += 1

    if not (e1 < s2 or s1 > e2):
        result_b += 1

print(result_a)
print(result_b)


