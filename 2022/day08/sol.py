with open('2022/day08/input.txt', 'r') as file:
    data = file.read()

lines = data.split('\n')

graph = []
for line in lines:
    graph.append(line)

directions = [(-1,0),(0,1),(1,0),(0,-1)]

n = len(graph)
m = len(graph[0])

result_a = 0
for r in range(n):
    for c in range(m):
        vis = False
        for (dr,dc) in directions:
            rr = r
            cc = c
            flag = True
            while True:
                rr += dr
                cc += dc
                if  not (0 <= rr < n and 0 <= cc < m):
                    break
                if(graph[rr][cc] >= graph[r][c]):
                    flag = False
            if flag:
                vis = True
        if vis:
            result_a += 1
        
print(result_a)

result_b = 0

for r in range(n):
    for c in range(m):
        trees = 1
        for (dr, dc) in directions:
            rr = r + dr
            cc = c + dc
            count = 1
            while True:
                if not (0 <= rr < n and 0 <= cc < m):
                    count -= 1
                    break
                if (graph[rr][cc] >= graph[r][c]):
                    break
                count += 1
                rr += dr
                cc += dc
            trees *= count
        result_b = max(result_b, trees)
print(result_b)
        





