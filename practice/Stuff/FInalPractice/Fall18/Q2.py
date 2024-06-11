sizeMatrix = int(input())
matList = []

for i in range(sizeMatrix):
    tempList = list(map(int, input().split()))
    matList.append(tempList)

for i in range(sizeMatrix-1 , -1, -1):
    for j in range(sizeMatrix-1, -1, -1):
        print(matList[i][j], end = ' ')
    print()