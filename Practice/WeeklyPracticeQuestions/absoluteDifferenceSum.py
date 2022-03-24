# Write the program that finds the sum of the absolute 
# values of the differences between two consecutive 
# elements in an integer list with N (2 <N <100) elements.
# No Imports

#Input:  5
#        10 9 8 3 9
#Output: 13

#Input:  10
#        10 12 8 5 7 14 20 2 9 21
#Output: 61

x = int(input())
intList = list(map(int, input().split()))
lastSum = 0

for i in range(x-1):
    if intList[i] > intList[i+1]:
        lastSum = lastSum + (intList[i] - intList[i+1])
    else:
        lastSum = lastSum + (intList[i+1] - intList[i])
print(lastSum)