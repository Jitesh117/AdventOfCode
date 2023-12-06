with open('day02/input.txt', 'r') as file:
    data = file.read()

result_a = 0
result_b = 0
for x in data.split('\n'):
    opp,me = x.split()
    result_a += {'X': 1, 'Y': 2, 'Z': 3}[me]
    result_a += {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
            ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
            ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
            }[(opp, me)]

    result_b += {'X': 0, 'Y': 3, 'Z': 6}[me]
    result_b += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
            ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
            ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
            }[(opp, me)]
print(result_a)
print(result_b)
