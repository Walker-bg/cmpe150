#In Fibonacci Numbers, each number progresses as the
#  sum of the two preceding numbers, such as 
# 0,1,1,2,3,5,8, ... In this question you are given a 
# number (0 <N <20). Accordingly, write the program that 
# prints all Fibonacci numbers backwards from the Nth Fibonacci number.

#Input: 0
#Output: 0

#Input: 5
#Output: 5 3 2 1 1 0

#Input: 10
#Output: 55 34 32 13 8 5 3 2 1 1 0

x = int(input())
fibList = []
m = 0
k = 1

fibList.append(m)
for i in range(x):
    fibList.append(k)
    temp = k
    k = m + k
    m = temp
    
for ij in range(1, len(fibList)+1):
    print(fibList[-ij], end = ' ') 