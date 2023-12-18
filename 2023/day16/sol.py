f = open("2023/day16/input.txt").read().splitlines()
import time

def debugData(tData):
  for x in tData:
    line = ''
    for y in x:
      if y == 0: char = '.'
      else:
        if y in [3,5,7,11]: char = '#'
        elif y == 3*5*7*11: char = '!'
        else: char = 'X'
      line = line + char
    print(line)


start = time.time()

data= [list(var) for var in f]

prims = [2,3,5,7,11]

def findCnt(beams):
  tData = []
  for x in data:
    line = [0 for _ in x]
    tData.append(line)
  cnt = 0
  while True:
    if len(beams) == 0: break
    for idx, beam in reversed(list(enumerate(beams))):
      i,j,dir = beam[0], beam[1], beam[2]
      if i < 0 or i > len(data[0])-1 or j < 0 or j > len(data)-1:
        del beams[idx]
        continue
      
      cellVal = tData[i][j]
      if cellVal == 0:
        cnt += 1
        tData[i][j] = prims[dir]
      else:
        mod = cellVal % prims[dir]
        if mod != 0:
          tData[i][j] *= prims[dir]
        else: 
          del beams[idx]
          continue
        
      if data[i][j] == ".":
        if dir == 1:   i = i-1
        elif dir == 2: j = j+1
        elif dir == 3: i = i+1
        elif dir == 4: j = j-1
    
      elif data[i][j] == '|':
        if dir in [2,4]:
          beams.append([i-1,j,1])
          beams.append([i+1,j,3])
          del beams[idx]
          continue
        else:
          if dir == 1: i = i-1
          else: i = i+1
      elif data[i][j] == '-':
        if dir in [1,3]:
          beams.append([i,j-1,4])
          beams.append([i,j+1,2])
          del beams[idx]
          continue
        else:
          if dir == 2: j = j+1
          else: j = j-1
      elif data[i][j] == '\\':
        if dir == 1: j,dir = j-1, 4
        elif dir == 2: i,dir = i+1,3
        elif dir == 3: j,dir = j+1,2
        elif dir == 4: i,dir = i-1, 1
      elif data[i][j] == '/':
        if dir == 1: j,dir = j+1, 2
        elif dir == 2: i,dir = i-1, 1
        elif dir == 3: j,dir = j-1, 4
        elif dir == 4: i, dir = i+1, 3
      beams[idx] = [i,j,dir]
  # debugData(tData)
  return cnt

def getMaxLight():
  max = 0
  print("0/4")
  for i in range(len(data[0])):
    res = findCnt([[0,i,3]])
    if res > max: max = res
  print("1/4")
  for i in range(len(data)):
    res = findCnt([[i,len(data[0])-1, 4]])
    if res > max: max = res
  print("2/4")
  for i in range(len(data[0])):
    res = findCnt([[len(data)-1, i, 1]])
    if res > max: max = res
  print("3/4")
  for i in range(len(data)):
    res = findCnt([[i,0,2]])
    if res > max: max = res
  return max

# My time and rank:
print("Part1: ", findCnt([[0,0,2]])) # 02:42:53   6908
print("Part2: ", getMaxLight()) # 03:13:56   6870

print("It took", time.time()- start, "seconds!")