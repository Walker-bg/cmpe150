string = input()
wordList = string.split()
wordCount = len(wordList)
charCount = 0 
for word in wordList:
    charCount += len(word.rstrip(',').rstrip('.').rstrip('.').rstrip('?').rstrip('!'))
print("Word Count: " + str(wordCount) + ", Character Count: " + str(charCount))
