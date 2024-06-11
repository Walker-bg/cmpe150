#You will be given the elements of A set with N elements 
# and B set with M elements (2 <= N, M <= 100). Write the 
# program that finds the elements of the A∩B set. In the 
# first line of the entry, the number N will be given, 
# followed by the elements of the A set. In the second line, 
# first the number M, then the elements of the set B will be 
# given. When printing the result on the output, you must 
# print the elements in the order they appear in set A. 
# Intersections are guaranteed not to be empty sets. 
# Set elements will only consist of alphabet letters and numbers.

#Input: 9 a b c d e 1 2 3 4
#       9 c d e f g 6 7 8 9
#Output: c d e

#Input:2 a b
#      2 b a
#Output: a b

a = input().split()
b = input().split()
timesA = int(a.pop(0))
timesB = int(b.pop(0))

for x in range(timesA):
    if a[x] in b:
        print(a[x], end =' ')