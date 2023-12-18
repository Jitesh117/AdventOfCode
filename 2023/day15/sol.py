f = open("2023/day15/input.txt").read().split(",")

def getResult(path):
    remainder = 0
    for x in path:
        currVal = ord(x)
        currVal += remainder
        currVal *= 17
        remainder = currVal % 256
    return remainder

cnt = 0
for x in f:
    result = getResult(x)
    cnt += result

print("Part1: ", cnt)

f = open("2023/day15/input.txt").read().split(",")

def getResult(path):
    remainder = 0
    for x in path:
        currVal = ord(x)
        currVal += remainder
        currVal *= 17
        remainder = currVal % 256
    return remainder

cnt = 0
# print(getResult("HASH",0))

boxes = [[] for _ in range(256)]

for x in f:
    if "=" in x:
        lenNo = int(x.split("=")[1])
        lenName = x.split("=")[0]
        remove = False
    else:
        lenNo = 0
        lenName = x.split("-")[0]
        remove = True
    boxNo = getResult(lenName)
    currBox = boxes[boxNo]
    if len(currBox) == 0 and not remove:
        boxes[boxNo].append([lenName, lenNo])
    else:
        changeHappened = False
        for i in range(len(currBox)):
            if boxes[boxNo][i][0] == lenName:
                changeHappened = True
                newVal = [lenName, lenNo]
                if remove:
                    del boxes[boxNo][i]
                else: boxes[boxNo][i] = newVal
                break
        if not changeHappened:
            if not remove:
                boxes[boxNo].append([lenName, lenNo])

cnt = 0
for idx,box in enumerate(boxes):
    for jdx,lens in enumerate(box):
        currVal = (idx+1)*(jdx+1)*lens[1]
        cnt += currVal
        # print(lens[0], " : ", currVal)

print("Part 2:",cnt)
