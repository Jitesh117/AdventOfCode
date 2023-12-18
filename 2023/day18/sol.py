data = open("2023/day18/input.txt").read().splitlines()

def getNewVertic(dir,cnt, idx):
  if dir in ['R',0] : return (idx[0],idx[1]+cnt)
  elif dir in ['D',1]: return (idx[0]+cnt,idx[1])
  elif dir in ['L',2]: return (idx[0],idx[1]-cnt)
  return (idx[0]-cnt,idx[1])

p1C,p2C,p1v,p2v,p1ec,p2ec = (0,0), (0,0),[], [], 0, 0
for x in data:
  dir1, p1cnt,dir2,p2cnt = x.split()[0], int(x.split()[1]), int(x.split()[2][-2:-1:] ),int(x.split()[2][2:7:],16)
  p1ec, p2ec = p1ec+p1cnt, p2ec+p2cnt
  p1C,p2C = getNewVertic(dir1,p1cnt,p1C), getNewVertic(dir2,p2cnt,p2C)
  p1v.append(p1C)
  p2v.append(p2C)

def getArea(vertices,sum1,sum2):
  for k in range(-1,len(vertices)-1, 1):
    (x1,y1), (x2,y2) = vertices[k], vertices[k+1]
    sum1,sum2 = sum1+x1*y2, sum2+ y1*x2
  return abs(sum1-sum2)/2

print("Part1:", int(getArea(p1v,0,0)+p1ec/2 +1))
print("Part2:", int(getArea(p2v,0,0) + p2ec/2 +1))