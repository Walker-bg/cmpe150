n = int(input())
wordDict = {}

for i in range(n):
    tempWord = input()
    wordDict[tempWord] = wordDict.get(tempWord, 0) + 1

isPrintable = False
for key, value in wordDict.items():
    if value == 1:
        print(key)
        isPrintable = True

if isPrintable == False:
    print(str(-1))
