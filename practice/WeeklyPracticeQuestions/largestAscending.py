# Write the program that finds the length 
# of the longest ascending consecutive sublist in an
# integer list with N (2 <N <100) elements.

#Input: 5
#       10 9 8 23 49
#Output: 3

#Input: 10
#       10 12 8 5 7 14 20 2 99 21
#Output: 4

x = int(input())
intList = list(map(int, input().split()))

maxAsc = 0
tempAsc = 0
for i in range(x-1):
    if (intList[i+1] - intList[i]) > 0:
        tempAsc += 1
    else:
        tempAsc = 0

    if (tempAsc+1) > maxAsc and tempAsc != 0:
        maxAsc = tempAsc+1

print(maxAsc)