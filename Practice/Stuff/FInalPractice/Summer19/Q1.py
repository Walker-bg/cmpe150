from decimal import Decimal
rodLenght, time = map(int, input().split())
beforeRod = list(map(Decimal , input().split()))
allTimesMatrix = []
afterRod = beforeRod.copy()

for i in range(time+1):
    allTimesMatrix.append(afterRod.copy())
    beforeRod = afterRod.copy()
    if rodLenght != 1:
        for index in range(rodLenght):
            if rodLenght == 1:
                pass
            elif index != 0 and index != rodLenght-1:
                afterRod[index] = round(((beforeRod[index] * 2) + beforeRod[index+1] + beforeRod[index-1]) / 4 , 1)

            elif index == rodLenght-1:
                afterRod[index] = round(((beforeRod[index] * 2) + beforeRod[index-1]) / 3 , 1)

            elif index == 0:
                afterRod[index] = round(((beforeRod[index] * 2) + beforeRod[index+1]) / 3 , 1)

for i in range(time+1):
    for j in range(rodLenght):
        print(allTimesMatrix[i][j], end = ' ')
    print()
