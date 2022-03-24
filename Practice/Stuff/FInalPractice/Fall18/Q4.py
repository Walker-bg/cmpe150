from decimal import Decimal
numOfRectangle = int(input())
areaList = []
for i in range(numOfRectangle):
    x, y = map(Decimal, input().split())
    areaList.append(x * y)
print(min(areaList))