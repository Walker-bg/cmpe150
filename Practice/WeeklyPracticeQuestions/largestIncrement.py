# Write the program that finds the largest positive 
# increment in an integer list with N (2 <N <100) elements.

#Input: 5
#       100 9 8 23 49
#Output: 26

#Input: 10
#       10 12 8 5 7 14 20 2 99 21
#Output: 97

x = int(input())
intList = list(map(int, input().split()))
maxInc = 0
for i in range(x-1):
    tempInc = intList[i+1] - intList[i]
    if tempInc > maxInc:
        maxInc = tempInc
print(maxInc)

