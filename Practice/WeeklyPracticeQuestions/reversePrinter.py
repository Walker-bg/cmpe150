#Write the given 10 integer numbers in reverse.

#Input: 3 6 9 12 15 18 21 24 27 30
#Output: 30 27 24 21 18 15 12 9 6 3

#Input: 0 1 2 3 4 5 6 7 8 9
#Output: 9 8 7 6 5 4 3 2 1 0

x = input()
xList = x.split()
for i in range(1, len(xList)+1):
    print(xList[-i], end = ' ')