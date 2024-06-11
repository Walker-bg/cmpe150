# In a 15-element list, find the maximum consecutively 
# repeating character, and print the number of repetition.

#Input: А 2 2 С с # A A A A 4 f f f F
#Output: 4

#Input: 4 h # 6 c c & 8 ( a t t Q Q $
#Output: 2

charList = input().split()

maxRep = 0
tempRep = 0
for i in range(len(charList)-1):
    if charList[i] == charList[i+1]:
        tempRep += 1
    else:
        tempRep = 0
    if (tempRep+1) > maxRep and tempRep != 0:
        maxRep = tempRep + 1
print(maxRep)