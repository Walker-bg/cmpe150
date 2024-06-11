
def subset(lst, subsetDict = {}):

    if len(lst) != 0:
        subsetDict.get(lst, 0)+=1
    else:
        return

    for i in range(len(lst)):
        tempList = lst.copy()
        del tempList[i]
        subset(tempList, subsetDict)

subset([1,2,3])
print(subsetDict)