import time
start_time = time.time()


inputFile = "2023/day14/input.txt"
data = []

def moveNorth():
  for j in range(len(data[0])):
    for i in range(len(data)):
      if data[i][j] == 'O':
        idx = i
        while True:
          if idx == 0: break
          if data[idx-1][j] != '.': break
          else:
            data[idx][j] = '.'
            data[idx-1][j] = 'O'
          idx -= 1

def moveSouth():
  for j in range(len(data[0])):
    for i in range(len(data)-1, -1, -1):
      if data[i][j] == 'O':
        idx = i
        while True:
          if idx == len(data)-1: break
          if data[idx+1][j] != '.': break
          else:
            data[idx][j] = '.'
            data[idx+1][j] ='O'
          idx += 1

def moveWest():
  for i in range(len(data)):
    for j in range(len(data[0])):
      if data[i][j] == 'O':
        idx = j
        while True:
          if idx == 0: break
          if data[i][idx-1] != '.': break
          else:
            data[i][idx] = '.'
            data[i][idx-1] = 'O'
          idx -=1 

def moveEast():
  for i in range(len(data)):
    for j in range(len(data[0])-1,-1,-1):
      if data[i][j] == 'O':
        idx = j
        while True:
          if idx == len(data[0]) -1: break
          if data[i][idx+1] != '.': break
          else:
            data[i][idx] = '.'
            data[i][idx+1] = 'O'
          idx += 1

def peformTurn():
  moveNorth()
  moveWest()
  moveSouth()
  moveEast()

def findSolution():
  cnt = 0
  for i,x in enumerate(data):
    for j in range(len(x)):
      if x[j] == 'O':
        cnt += len(data) -i
  return cnt

def completePart1():
  f = open(inputFile).read().splitlines()

  global data
  data = []
  for x in f:
    data.append(list(x))
  moveNorth()
  return findSolution()


def completePart2():

  f = open(inputFile).read().splitlines()
  global data
  data = []
  for x in f:
    data.append(list(x))

  for i in range(150):
    peformTurn()

  sols = []
  for i in range(50):
    peformTurn()
    result = findSolution()
    sols.append(result)

  period = 0
  for i in range(1,len(sols)):
    if sols[i] == sols[0] and sols[i+1] == sols[1] and sols[i+2] == sols[2]:
          period = i
          break
  return sols[999999850 % period -1]

# My time and rank
print("Part 1: ", completePart1()) # 00:21:15   3436
print("Part 2: ", completePart2()) # 02:05:14   4988


print("--- %s seconds ---" % (time.time() - start_time))