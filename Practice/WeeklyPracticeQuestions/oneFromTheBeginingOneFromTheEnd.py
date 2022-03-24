#In this problem you are given an even N (1 <N <100) number. 
# Then N integers are given. Write a program that prints these 
# given numbers such as one from beginning one from end and so on.

#Input:  6
#        1 2 3 4 5 6
#Output: 1 6 2 5 3 4

#Input:  2
#        1 5
#Output: 1 5

#Input:  4
#        12 14 15 13
#Output: 12 13 14 15

numOfInput = int(input())
y = input()
numList = y.split()
beg = 0
end = 1 

for i in range(1, len(numList)+1):
    if i%2==1:
        print(numList[beg], end = ' ')
        beg += 1
    else:
        print(numList[-end], end = ' ')
        end += 1
