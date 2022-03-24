# Strings that read in reverse are the same as themselves 
# are called palindromes. Find out if a string of 10 elements 
# given to you is a palindrome. If it is a palindrome, print
# 1 on the screen, otherwise 0.

#Input: i o n u r s u n o i
#Output: 0

#Input: n a z a n n a z a n
#Output: 1

x = input()
xList = x.split()

if xList == xList[::-1]:
    print(1)
else:
    print(0)