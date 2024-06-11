def letterCountMultiplier(string, stringDict = {}):
    if len(string)>0:
        stringDict[string[0]] = stringDict.get(string[0], 0) + 1
        return letterCountMultiplier(string[1:], stringDict)
    if len(string) == 0:
        if len(stringDict)==0:
            return 0
        else:
            multiple = 1
            for value in stringDict.values():
                multiple *= value
            return multiple
    

    

print(letterCountMultiplier('abababc', {}))
print(letterCountMultiplier('aaaaaa', {}))
print(letterCountMultiplier('a', {}))
print(letterCountMultiplier('', {}))
print(letterCountMultiplier('abb', {}))
print(letterCountMultiplier('ab', {}))
